import os, sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from myproject import Ui_MainWindow

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

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        super(MainWindow, self).setupUi(self)
        #print(dir(self.dockWidget_2))
        self.dockWidget_2.setTitleBarWidget(QWidget(None))
        #self.treeWidget = MyTreeWidget(self.treeWidget)
        #help(self.treeWidget.resizeEvent)
        #self.treeWidget.resizeEvent = MyTreeWidget.resizeEvent
        #self.dockWidget_2 = MyQDockWidget(self.dockWidget_2)
        #self.verticalLayout_2.resizeEvent = MyQVBoxLayout.resizeEvent

    def contextMenuEvent(self, event):
        self.menu = QMenu(self)
        renameAction = QAction('Rename', self)
        renameAction.triggered.connect(lambda: self.renameSlot(event))
        self.menu.addAction(renameAction)
        # add other required actions
        self.menu.popup(QCursor.pos())

if __name__ == '__main__':
    #import PyQt5
    #pyqt = os.path.dirname(PyQt5.__file__)
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    sys.exit(app.exec_())
