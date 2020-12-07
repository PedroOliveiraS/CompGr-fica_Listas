# PyQt 5 - Criando interfaces gráficas com o Python

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.x = 640
        self.y = 480
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Hello World - Comp Gráfica")

        # Criando um QLabel para o texto
        self.texto = QLabel("Hello World from PyQt5 - IFTM", self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        self.texto.move((self.x / 2) - (self.largura /2), (self.y / 4) - (self.altura / 2))

        # Criando um botão
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me?")
        self.xb1 = int(self.x/2 - self.largura/2 + 25)
        self.yb1 = int(self.x / 4 - self.largura / 2 + 50)
        self.b1.move(self.xb1, self.yb1)
        self.b1.clicked.connect(self.button_clicked)

        # Criando uma imagem
        self.imagem1 = QLabel(self)
        self.endereco = QtGui.QPixmap('images/balao_colorido.jpg')
        self.imagem1.setPixmap(self.endereco)
        self.imagem1.setGeometry(self.x /2 - 100, self.yb1+50, 200, 200)

    # Método para ação do botão
    def button_clicked(self):
        self.texto.setText("Botão foi clicado!?")
        self.texto.adjustSize()
        self.novoEndereco = QtGui.QPixmap('images/balao_grayscale.jpg')
        self.imagem1.setPixmap(self.novoEndereco)



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()