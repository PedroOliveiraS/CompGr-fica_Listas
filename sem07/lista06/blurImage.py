# Importar as bibliotecas
from PIL import Image, ImageFilter

def run():

    # Abrir a Imagem
    img1 = Image.open('images/colored.jpg')

    # Aplicar o filtro Blur
    # Esse filtro aplica um efeito de embaçamento / enevoamento na imagem
    img2 = img1.filter(ImageFilter.BLUR)

    # Salvar a imagem resultante
    img2.save('images/blurImage.jpg')

if __name__ == "__main__":
    run()