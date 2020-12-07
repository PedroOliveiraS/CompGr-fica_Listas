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
        self.x = 450
        self.y = 360
        self.setMinimumSize(QSize(self.x, self.y))
        #self.setWindowTitle("Hello World - Comp Gráfica")

        # Criando um QLabel para o texto
        self.texto = QLabel("Processamento Digital de Imagens", self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        print(self.largura)
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        self.texto.move((self.x / 2) - (self.largura /2), (self.y / 2 )- (self.altura / 2))

        # Criando um botão
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me?")
        self.b1.setGeometry(20,self.y - 30, self.x - 40, 20)
        self.b1.clicked.connect(self.button_clicked)


    # Método para ação do botão
    def button_clicked(self):
        self.texto.setText("Pedro Oliveira")
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.move((self.x / 2) - (self.largura / 2), (self.y / 2) - (self.altura / 2))



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()