#!/usr/bin/env python3

import minidb

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableView, QMessageBox
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery

from utils import getLocalPath

class Downloads(minidb.Model):
	url = str
	filename = str
	status = str
	size = int
	description = str

def createConnection():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('downloads.db')
    if not db.open():
        QMessageBox.critical(None, "Cannot open database",
                "Unable to establish a database connection.\n",
                QMessageBox.Cancel)
        return False

    return True

def initializeModel():
    model = QSqlTableModel()
    model.setTable('Downloads')

    model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    model.select()

    #model.setHeaderData(0, Qt.Horizontal, "URL")
    #model.setHeaderData(1, Qt.Horizontal, "Filename")
    #model.setHeaderData(2, Qt.Horizontal, "Status")
    #model.setHeaderData(3, Qt.Horizontal, "Size")
    #model.setHeaderData(4, Qt.Horizontal, "Description")
    return model

def bindView(title, view, model):
    view.setModel(model)
    #view.setWindowTitle(title)

def createDb():
    db = minidb.Store(getLocalPath("downloads.db"))
    db.register(Downloads)
    db.close()
