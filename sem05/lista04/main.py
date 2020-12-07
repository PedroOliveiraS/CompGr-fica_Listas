# Imports relacionados a questão 1
from sem05.lista04 import detBord01
from sem05.lista04 import detBord02
from sem05.lista04 import detBord03
from sem05.lista04 import sharpen_blur

def run01():
    detBord01.filtro01()
    detBord02.filtro02()
    detBord03.filtro03()

def run02():
    sharpen_blur.run()

if __name__ == "__main__":
    run01()

    run02()