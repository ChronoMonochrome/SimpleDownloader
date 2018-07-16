#!/usr/bin/env python3

import os, sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from utils import getLocalPath

from models import downloads

def resizeEvent(self, event):
    width = event.size().width()
    self.setColumnWidth(1, 100)
    self.setColumnWidth(2, width - 100)

class MyTreeWidget(QTreeWidget):
    def __init__(self, parent = None):
        self.parent = parent
        super(MyTreeWidget, self).__init__(parent)

    def resizeEvent(self, event):
        width = event.size().width()
        print("event width: %d" % width)

class MyQDockWidget(QDockWidget):
    def __init__(self, parent):
        super(MyQDockWidget, self).__init__(parent)
        parent.setTitleBarWidget(QWidget(None))

class MyQVBoxLayout(QVBoxLayout):
    def __init__(self, parent = None):
        self.parent = parent
        super(QVBoxLayout, self).__init__(parent)

    def resizeEvent(self, event):
        self.parent.resizeEvent(event)
        width = event.size().width()
        print("event width: %d" % width)

class MainWindow(QMainWindow):
    def __init__(self, ui_path):
        super().__init__()
        uic.loadUi(ui_path, self)
        self.setupUi()

    def setupUi(self):
        self.dockWidget_2.setTitleBarWidget(QWidget(None))
        self.downloads = downloads.Downloads()
        self.downloads.createDb()
        if not self.downloads.createConnection():
            print("error")

        self.downloadsModel = self.downloads.initializeModel()
        self.downloads.bindView("Table Model (View 1)", self.tableView, self.downloadsModel)
        self.tableView.setColumnHidden(0, True)

        self.menu = QMenu(self)
        self.menu.addAction(self.actionAdd)

    def contextMenuEvent(self, event):
        self.menu.popup(QCursor.pos())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainWindow(getLocalPath("myproject.ui"))
    view.show()
    sys.exit(app.exec_())
