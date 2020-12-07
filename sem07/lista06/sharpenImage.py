# Importar as bibliotecas
from PIL import Image, ImageFilter

def run():

    # Abrir a Imagem
    img1 = Image.open('images/colored.jpg')

    # Aplicar o filtro de sharpen
    # O filtro de sharpen aumenta a nitidez das regiões presentes em uma imagem
    img2 = img1.filter(ImageFilter.SHARPEN)

    # Salvar a imagem resultante
    img2.save('images/sharpenImage.jpg')

if __name__ == "__main__":
    run()