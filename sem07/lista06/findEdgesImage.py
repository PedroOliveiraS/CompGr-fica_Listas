# Importar as bibliotecas
from PIL import Image, ImageFilter

def run():

    # Abrir a Imagem
    img1 = Image.open('images/colored.jpg')

    # Aplicar o filtro de Find Edges
    # Esse filtro tem como objetivo denotar as bordas das regiões presentes na imagem
    img2 = img1.filter(ImageFilter.FIND_EDGES)

    # Salvar a imagem resultante
    img2.save('images/findEdgesImage.jpg')

if __name__ == "__main__":
    run()