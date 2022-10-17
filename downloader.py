from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from pytube import YouTube

app = QApplication([])

#icon = "YouTube_icon.png"
window = QWidget()
window.setWindowTitle("YouTube downloader")
window.setWindowIcon(QtGui.QIcon('image//icon.ico'))
window.move(500,200)
window.resize(300,200)
window.show()

text_file1 = QLineEdit()
text_file2 = QLineEdit()

label_1 = QLabel("URL:")
label_2 = QLabel("forder path:")
label_3 = QLabel("Please write the url of vidio")
button_1 = QPushButton("start")
button_1.size()

v_line = QVBoxLayout()
v_line.addWidget(label_1, 1, alignment=Qt.AlignTop)
v_line.addWidget(text_file1, 1, alignment=Qt.AlignTop)
v_line.addWidget(label_2, 1, alignment=Qt.AlignTop)
v_line.addWidget(text_file2, 1, alignment=Qt.AlignTop)

v_line.addWidget(button_1)
v_line.addWidget(label_3, 0, alignment=Qt.AlignBottom)
window.setLayout(v_line)

def start():
    forder = str(text_file2.text())
    url_of_vidio = text_file1.text()
    link = url_of_vidio
    vid = YouTube(link)
    label_3.setText("Loading")
    print("Downloading" , vid.title)
    print("Views: ", vid.views)
    print("Length: ", vid.length, "seconds")
    print("Description: ", vid.description)
    print("Ratings: ", vid.rating)
    vid_download = vid.streams.get_by_itag('22')
    vid_download.download(forder)
    print("completed")
    label_3.setText("Finish")

button_1.clicked.connect(start)

app.exec()
























