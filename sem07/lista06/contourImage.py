# Importar as bibliotecas
from PIL import Image, ImageFilter

def run():

    # Abrir a Imagem
    img1 = Image.open('images/colored.jpg')

    # Aplicar o filtro de Contour
    # A aplicação desse filtro resulta em uma imagem preto e branco, destacando os contornos entre os objetos
    # / personagens presentes na imagem
    img2 = img1.filter(ImageFilter.CONTOUR)

    # Salvar a imagem resultante
    img2.save('images/contourImage.jpg')

if __name__ == "__main__":
    run()