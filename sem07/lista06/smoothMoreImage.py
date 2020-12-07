# Importar as bibliotecas
from PIL import Image, ImageFilter

def run():

    # Abrir a Imagem
    img1 = Image.open('images/colored.jpg')

    # Aplicar o filtro de Smooth more
    # O filtro aplica uma redução ainda maior de nitidez nas bordas das diferentes regiões presentes na imagem
    img2 = img1.filter(ImageFilter.SMOOTH_MORE)

    # Salvar a imagem resultante
    img2.save('images/smoothMoreImage.jpg')

if __name__ == "__main__":
    run()