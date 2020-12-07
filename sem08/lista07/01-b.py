## b) Somente o layout. Os botões não tem ações vinculadas
#
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.x = 630
        self.y = 250
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Given")

        # Criando o botão 01
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Original")
        self.b1.setGeometry(10,200, 300, 30)

        # Criando o botão 02
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Transformado")
        self.b2.setGeometry(320, 200, 300, 30)

        # Criando a imagem 01
        self.image01 = QLabel(self)
        self.end01 = QtGui.QPixmap('images/original_colored.jpg')
        self.image01.setPixmap(self.end01)
        self.image01.setGeometry(10,20, 300, 168)

        # Criando a imagem 02
        self.image02 = QLabel(self)
        self.end02 = QtGui.QPixmap('images/original_grayscale.jpg')
        self.image02.setPixmap(self.end02)
        self.image02.setGeometry(320, 20, 300, 168)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()