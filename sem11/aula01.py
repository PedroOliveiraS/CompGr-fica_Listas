# PyQt 5 - Criando interfaces gráficas com o Python

import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_main_window()
        self.initUI()

    def setup_main_window(self):
        self.x = 640
        self.y = 480
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Hello World - Comp Gráfica")
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.layout = QGridLayout()
        self.wid.setLayout(self.layout)

    def initUI(self):
        # Criar a barra de menu
        self.barraDeMenu = self.menuBar()

        # Criar os menus
        self.menuArquivo = self.barraDeMenu.addMenu("&Arquivo")
        self.menuImagens = self.barraDeMenu.addMenu("&Imagens")
        self.menuSobre = self.barraDeMenu.addMenu("&Sobre")

        # Criar as actions
        self.opcaoAbrir = self.menuArquivo.addAction("&Abrir")
        self.opcaoAbrir.triggered.connect(self.open_file)
            #Atalho
        self.opcaoAbrir.setShortcut("Ctrl+A")
        self.opcaoAbrir.setCheckable(True)
        self.opcaoAbrir.setChecked(True)

        self.opcaoRecentes = self.menuArquivo.addMenu("&Recentes")
        self.opcaoAbrirRecente = self.opcaoRecentes.addAction("&Abrir recentes...")
        self.menuArquivo.addSeparator() #


        self.opcaoFechar = self.menuArquivo.addAction("F&echar")
        self.opcaoFechar.setShortcut("Ctrl+X")
        self.opcaoFechar.triggered.connect(self.close)

        self.opcaoSobre = self.menuSobre.addAction("Sobre")
        self.opcaoSobre.triggered.connect(self.exibe_mensagem)
        self.opcaoApagar = self.menuSobre.addAction("Apagar")
        self.opcaoApagar.triggered.connect(self.apagar_mensagem)
        # Criar a barra de status
        self.barraDeStatus = self.statusBar()
        self.barraDeStatus.showMessage("Oi, bem vindo ao programa")

        # Criar os outros widgets (Label, Button, Text, Image)
        # Criando um QLabel para o texto
        self.texto = QLabel("Hello World from PyQt5 - IFTM", self)
        self.texto.adjustSize()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        # Criando os botões
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Open me")
        self.b1.clicked.connect(self.open_file)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Transforme me?")
        self.b2.clicked.connect(self.transform_me)

        # Criando as imagens
        self.imagem1 = QLabel(self)
        self.endereco1 = 'images/balao_colorido.jpg'
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

        self.imagem2 = QLabel(self)
        self.endereco2 = 'images/balao_grayscale.jpg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

        # Organizando os widgets dentro do gridLayout
        self.layout.addWidget(self.texto, 0, 0, 1, 2)
        self.layout.addWidget(self.b1, 2, 0)
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.setRowStretch(0, 0)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 0)

    # Método para ações dos botões
    def open_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                            caption='Open image',
                                                            directory=QtCore.QDir.currentPath(),
                                                            filter='All files (*.*);; Images (*.jpg;*.png)',
                                                            initialFilter='Images (*.jpg;*.png)')
        print(fileName)
        if fileName != ' ':
            self.endereco1 = fileName
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)

    def transform_me(self):
        self.entrada = self.endereco1
        self.saida = 'images/arquivo_novo.jpg'
        self.script = '.\colored_to_grayscale.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def exibe_mensagem(self):
        # self.barraDeStatus.showMessage("Você clicou no sobre")
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Desenvolvido por Marsh")
        self.msg.setWindowTitle("Sobre")
        self.msg.setInformativeText("Ituiutaba - 19/11/2020\nIFTM")
        self.msg.setDetailedText("Texto  com mais detalhes sobre esse aplicativo")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_() # Exibe a caixa de texto | Caixa de diálogo
        self.reply = self.msg.clickedButton()
        self.barraDeStatus.showMessage("Foi clicado o botão " + self.reply.text())

        if self.reply.text() == "OK":
            print("Apertou OK")
        if self.reply.text() == "Cancel":
            print("Apertou Cancel")

    def apagar_mensagem(self):
        self.barraDeStatus.clearMessage()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()