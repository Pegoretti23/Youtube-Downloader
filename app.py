from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import pytube


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YT Downloader")
        self.setGeometry(100, 100, 300, 300)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        #creating URL input 
        self.userinput = QLineEdit(self)
        self.userinput.setGeometry(20, 120, 271, 23)
        #creating a folder button
        self.dirName = QPushButton("Select Folder", self)
        self.dirName.setGeometry(80, 170, 151, 23)
        self.dirName.clicked.connect(self.folder)
        # creating a push button
        self.button = QPushButton("Download", self)
        self.button.setGeometry(120, 200, 75, 23)
        self.button.clicked.connect(self.clickme)


    # action method
    def folder(self):
        self.folder = QFileDialog.getExistingDirectory(self, "Select Folder")



    def clickme(self):
        userurl = self.userinput.text()
        yt = pytube.YouTube(userurl)
        stream = yt.streams.get_highest_resolution()
        try:
            stream.download(output_path=self.folder, filename=None)
            QMessageBox.question(self, 'Status', "Download Complete",QMessageBox.Ok)
        except:
            QMessageBox.question(self, 'Status', "Select one Folder",QMessageBox.Ok)
        
    

  



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())