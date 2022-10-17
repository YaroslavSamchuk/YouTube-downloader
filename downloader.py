from asyncio import events
from multiprocessing import Event
import time
from PyQt5.QtCore import Qt
import os
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMainWindow
from pyautogui import click
from pytube import *
import sys

#elements

#elements

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube downloader")
        self.setWindowIcon(QtGui.QIcon('image//icon.ico'))
        self.setGeometry(700, 400, 300, 200)
        self.show()
        
    def window1(self):
        text_file1 = QLineEdit()
        text_file2 = QLineEdit()
        label_1 = QLabel("URL:")
        label_2 = QLabel("forder path:")
        label_3 = QLabel("Please write the url of vidio")
        button_1 = QPushButton("start")
        v_line = QVBoxLayout()
        v_line.addWidget(label_1, 1, alignment=Qt.AlignTop)
        v_line.addWidget(text_file1, 1, alignment=Qt.AlignTop)
        v_line.addWidget(label_2, 1, alignment=Qt.AlignTop)
        v_line.addWidget(text_file2, 1, alignment=Qt.AlignTop)
        v_line.addWidget(button_1)
        v_line.addWidget(label_3, 0, alignment=Qt.AlignBottom)
        self.setLayout(v_line)

        def start(self):
            label_3.setText("Loading")
            link = text_file1.text()
            vid = YouTube(link)
            print("Downloading ", vid.title)
            print("Views: ", vid.views)
            print("Length: ", vid.length, "seconds")
            print("Description: ", vid.description)
            print("Ratings: ", vid.rating)
            vid_download = vid.streams.get_by_itag('22')
            vid_download.download(text_file2.text())
            print("completed")
            text_file1.clear()
            text_file2.clear()
            label_3.setText("Finish!")
            if click():
                label_3.setText("Please write the url of vidio")
        button_1.clicked.connect(start)
        
app = QApplication([])

window = Window()
window.show()
window.window1()
sys.exit(app.exec())