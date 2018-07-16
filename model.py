#!/usr/bin/env python3

import minidb

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableView, QMessageBox
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery

from utils import getLocalPath

class Model(object):
    def __init__(self):
        className = self.__class__.__name__
        self.databaseName = "%s.db" % (className.lower())
        self.tableName = className

    def createConnection(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(self.databaseName)
        if not db.open():
            QMessageBox.critical(None, "Cannot open database",
                    "Unable to establish a database connection.\n",
                    QMessageBox.Cancel)
            return False

        return True

    def initializeModel(self):
        model = QSqlTableModel()
        model.setTable(self.tableName)

        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.select()

        #model.setHeaderData(0, Qt.Horizontal, "URL")
        #model.setHeaderData(1, Qt.Horizontal, "Filename")
        #model.setHeaderData(2, Qt.Horizontal, "Status")
        #model.setHeaderData(3, Qt.Horizontal, "Size")
        #model.setHeaderData(4, Qt.Horizontal, "Description")
        return model

    def bindView(self, title, view, model):
        view.setModel(model)
        #view.setWindowTitle(title)

    def createDb(self):
        db = minidb.Store(getLocalPath(self.databaseName))
        db.register(self.__class__)
        db.close()
