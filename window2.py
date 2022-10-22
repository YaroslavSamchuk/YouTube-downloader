from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from pytube import *
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5 import QtWidgets
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QMenu
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QPlainTextEdit
from PyQt5.QtGui import QIcon


class Window2(QMainWindow, object):
    def __init__(self):
        super(Window2, self).__init__()
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle("Console")
        self.setStyleSheet("background-color: Black;")

        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.setStyleSheet("color: rgb(19, 161, 14);")
        self.setCentralWidget(self.text_edit)
        self.createMenuBar()
        self.show()
    

    def print_info_vidio(self, one, two, three, four, five):
        self.text_edit.setText("Title: " + one + "\n" + "Number of views: " + two + "\n" + "Length: " + three + "seconds" + "\n" "Description: " + "\n" + four + "\n" + "Raitings: " + five)

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.menuBar.setFont(QFont('Console', 10))
        self.setMenuBar(self.menuBar)
        self.menuBar.setStyleSheet("background-color: White;")

        self.text_edit.setFont(QFont('Console', 10))
        
        

        fileMenu = QMenu("&Help", self)
        fileMenu.setFont(QFont('Console', 10))
        fileMenu.setStyleSheet("background-color: Gray;")
        fileMenu.setIcon(QIcon("image/info.png"))

        clearMenu = QMenu("&Clear", self)
        clearMenu.setFont(QFont('Console', 10))
        clearMenu.setStyleSheet("background-color: Gray;")
        clearMenu.setIcon(QIcon("image/clear.png"))

        #clear_all = QAction("&Clear All", self)
        #clear_all.setIcon(QIcon("image/clear_1.png"))
        
        self.menuBar.addMenu(fileMenu)
        #self.menuBar.addSeparator()
        self.menuBar.addMenu(clearMenu)
        clearMenu.addAction("Clear All", self.clear_text)
        
        #info_file = fileMenu.addMenu("&InfoProgram")
        #help_file = fileMenu.addMenu("&HelpProgram")
        #exit_file = fileMenu.addMenu("&Exit")

        fileMenu.addAction("InfoProgram", self.info_program)
        fileMenu.addSeparator()
        fileMenu.addAction("HelpProgram", self.help_program)
        #clear_all = clearMenu.addAction("Clear_All", self.clear_text)
        
        

    @QtCore.pyqtSlot()
    def info_program(self):
        self.text_edit.setText("YouTube downloader is the aplication that can download videos from YouTube!\nYarbro Team does not take reponsibility for you actions!\nClear the text?")

        #action = self.sender()
        #if action.text()== "InfoProgram":
        #    fname = QFileDialog.getOpenFileName(self)[0]
        #    try:
        #        f = open(fname, 'r')
        #        with f:
        #            data = f.read()
        #            self.text_edit.setText(data)
        #    except FileNotFoundError:
        #        self.text_edit.setText("Not such file")

    @QtCore.pyqtSlot()
    def help_program(self):
        self.text_edit.setText("If you have problem, please check the url or forder\nIf there is still an error please contact me:\n🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱")

    @QtCore.pyqtSlot()
    def clear_text(self):
        self.text_edit.setText("")
    
    @QtCore.pyqtSlot()
    def change_quality(self):
        pass