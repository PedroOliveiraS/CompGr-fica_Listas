## a) Ao clicar no botão “Click aqui!”, alterar o texto do QLabel para o seu nome completo.
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
        self.cont = 0

        self.x = 380
        self.y = 380
        self.setMinimumSize(QSize(self.x, self.y))
        #self.setWindowTitle("Hello World - Comp Gráfica")

        # Criando a QLabel para o texto do contador
        self.texto = QLabel(str(self.cont), self)
        self.texto.setFont(QtGui.QFont("Arial", 30))
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        self.texto.move((self.x / 2) - (self.largura /2), (self.y / 2 - 50 )- (self.altura / 2))

        # Criando o botão 1 (Increment)
        self.b01 = QtWidgets.QPushButton(self)
        self.b01.setText("[+] Increment")
        self.b01.setGeometry(-10,self.y/2 + 70, self.x+10, 30)
        self.b01.clicked.connect(self.button_increment)

        # Criando o botão 2 (Decrement)
        self.b01 = QtWidgets.QPushButton(self)
        self.b01.setText("[-] Decrement")
        self.b01.setGeometry(-10, self.y / 2 + 105, self.x + 10, 30)
        self.b01.clicked.connect(self.button_decrement)

        # Criando o botão 1 (Reset)
        self.b01 = QtWidgets.QPushButton(self)
        self.b01.setText("[«] Reset")
        self.b01.setGeometry(-10, self.y / 2 + 140, self.x + 10, 30)
        self.b01.clicked.connect(self.button_reset)

    # Método para ação do botão
    def button_increment(self):
        self.cont = self.cont + 1
        self.texto.setText(str(self.cont))
        self.texto.adjustSize()


    def button_decrement(self):
        if(self.cont > 0):
            self.cont = self.cont - 1
            self.texto.setText(str(self.cont))
            self.texto.adjustSize()

    def button_reset(self):
        self.cont = 0
        self.texto.setText(str(self.cont))

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()