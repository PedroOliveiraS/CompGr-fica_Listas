# Importar as bibliotecas
from PIL import Image, ImageFilter

def run():

    # Abrir a Imagem
    img1 = Image.open('images/colored.jpg')

    # Aplicar o filtro de Detail
    # A aplicação desse filtro melhora os detalhes e cores da imagem, dando uma maior nitidez a diferentes áreas
    img2 = img1.filter(ImageFilter.DETAIL)

    # Salvar a imagem resultante
    img2.save('images/detailImage.jpg')

if __name__ == "__main__":
    run()