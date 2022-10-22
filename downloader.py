from distutils import text_file
from turtle import width
from urllib.error import URLError
import PyQt5
from PyQt5.QtCore import Qt
import os
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMainWindow
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from pytube import *
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication
from PyQt5.QtWidgets import QAction
from window2 import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QMessageBox
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtCore import QUrl
import sys

#elements

#elements

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube downloader")
        self.setWindowIcon(QtGui.QIcon('image//icon.ico'))
        self.setGeometry(900, 300, 300, 200)
        #self.setFixedSize(300, 200)
        #self.move(900, 300)
        self.complete = QMessageBox()
        self.complete.setText("Finish!")
        
        self.show()
        #---
        self.complete.hide()
        #---
        
    def window1(self):
        self.comboBox = QComboBox(self)
        self.element1 = self.comboBox.addItem("720", 0)
        self.element2 = self.comboBox.addItem("360", 1)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(0, 0, 300, 25)
        self.text_file1 = QLineEdit()
        self.text_file2 = QPushButton("Choose Forder")
        self.label_1 = QLabel("URL:", self)
        self.label_1.setGeometry(10, 28, 300, 20)
        self.label_1.setObjectName(u"Label_1")
        label_2 = QLabel("forder path:")
        self.label_3 = QLabel("Please write the url of vidio")
        button_1 = QPushButton("start")
        v_line = QVBoxLayout()
        #v_line.addWidget(self.comboBox, 1, alignment=Qt.AlignTop)
        #v_line.addWidget(label_1, 1, alignment=Qt.AlignBottom)
        v_line.addWidget(self.text_file1, 1, alignment=Qt.AlignBottom)
        v_line.addWidget(label_2, 0, alignment=Qt.AlignBottom)
        v_line.addWidget(self.text_file2, 0, alignment=Qt.AlignBottom)
        v_line.addWidget(button_1)
        v_line.addWidget(self.label_3, -2, alignment=Qt.AlignBottom)
        self.setLayout(v_line)
        self.video_itag = '22'
        

        self.comboBox.activated[str].connect(self.onactive)

        #show---
        self.show()
        self.comboBox.show()
        self.label_1.show()
        #show---

        
            #self.lbl.adjustSize()

        #def video_quality():
        #    if self.video_itag == '22':
        #        self.video_itag = '18'
        #        print(self.video_itag)
        #        stop(100)
        #    if self.video_itag == '18':
        #        self.video_itag = '22'
        #        print(self.video_itag)
            
        button_1.clicked.connect(self.start)
        self.text_file2.clicked.connect(self.choose_forder)
        #def video_quality360():
        #    self.video_itag = '22'
        #    print(self.video_itag)
        #first = self.comboBox.addAction(QAction("720p", video_quality360()))
        
        #self.comboBox.addAction(QAction("360p", video_quality360(self.video_itag)))

    def start(self):
        try:  
            link = str(self.text_file1.text())
            window2.text_edit.setText("Loading")
            try:
                vid = YouTube(link)
            except:
                window2.text_edit.setText("Please check the url")
            try:
                one = str(vid.title)
                two = str(vid.views)
                three = str(vid.length)
                four =  str(vid.description)
                five = str(vid.rating)
                window2.print_info_vidio(one, two, three, four, five)
            except:
                window2.text_edit.setText("Video if faulty")
            try:
                vid_download = vid.streams.get_by_itag(self.video_itag)
                vid_download.download(self.forder)
            except:
                window2.text_edit.setText("Video downloading ERROR")
            
            self.text_file1.clear()
            self.complete.show()

        except:
            self.label_3.setText("ERROR")
        
        
        #self.comboBox.activated.connect(video_quality360)
        #self.comboBox.currentIndexChanged.connect(video_quality)
        
        
    def onactive(self, text):
        if text == "720":
            self.video_itag = "22"
            print(self.video_itag)
        if text == "360":   
            self.video_itag = "18"
            print(self.video_itag)
    
    def choose_forder(self):
        try:
            action = self.sender()
            ford = QFileDialog.getExistingDirectory()
            self.forder = ford
            print(self.forder)
        except FileNotFoundError:
            window2.text_edit.setText("Not such file")
    #def _createMenuBar(self):
    #    menubar = self.menuBar()
    #    fileMenu = menubar.addMenu('File')
#
    #    impMenu = QMenu('Import', self)
    #    impAct = QAction('Import mail', self)
    #    impMenu.addAction(impAct)
#
    #    newAct = QAction('New', self)
#
    #    fileMenu.addAction(newAct)
    #    fileMenu.addMenu(impMenu)
#
    #    self.setGeometry(300, 300, 300, 200)
    #    self.setWindowTitle('Submenu')
    #    self.show()
        
#class MenuBar(QMainWindow):
#    def __init__(self):
#        super().__init__()
#        self.setGeometry(300, 400, 300, 200)
#        self.setStyleSheet("background-color: Black;")
#        self.show()
#    
#    def help(self):
#        label1 = QLabel("It is application")
#        v_line2 = QVBoxLayout()
#        v_line2.addWidget(label1)
#        self.setLayout(v_line2)
#
#    def mymenubar(self):
#        menubar = self.menuBar()
#        menubar.setStyleSheet("background-color: White;")
#        fileMenu = menubar.addMenu('File')
#        fileMenu2 = menubar.addMenu('Help')
#        impMenu = QMenu('Import', self)
#        image = 'image//icon.ico'
#        fileMenu2.setIcon(QtGui.QIcon('image//icon.ico'))
#        impAct = QAction('Import mail', self)
#        impMenu.addAction(impAct)
#        newAct = QAction('New', self)
#        fileMenu.addAction(newAct)
#        fileMenu.addMenu(impMenu)
#        self.setGeometry(300, 300, 300, 200)
#        self.setWindowTitle('Console')
#        self.label1 = QLabel("Hello", self)
#        self.label1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
#        self.label1.setStyleSheet("color: White;")
#        self.label1.setGeometry(50, 50, 50, 50)
#        self.show()
    
app = QApplication(sys.argv)   
window = Window()
window.window1()
window.show()
window2 = Window2()
window2.show()

sys.exit(app.exec())