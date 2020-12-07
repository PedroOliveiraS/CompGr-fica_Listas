# Importar as bibliotecas
from PIL import Image, ImageFilter

def run():

    # Abrir a Imagem
    img1 = Image.open('images/colored.jpg')

    # Aplicar o filtro de Smooth
    # O filtro aplica uma redução de nitidez nas bordas das diferentes regiões presentes na imagem
    img2 = img1.filter(ImageFilter.SMOOTH)

    # Salvar a imagem resultante
    img2.save('images/smoothImage.jpg')

if __name__ == "__main__":
    run()