import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

from PyQt5 import uic

form_class = uic.loadUiType("GUI/Qt/MoreInfo.ui")[0]

class InfoWindow(QMainWindow, form_class):
    def __init__(self, parent=None):
        super(InfoWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.setWindowIcon(QIcon("Images/favicon.png"))
        self.setFixedSize(self.size())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = InfoWindow()
    myWindow.show()
    sys.exit(app.exec_())
