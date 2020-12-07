# Importar as bibliotecas
from PIL import Image, ImageFilter

def run():

    # Abrir a Imagem
    img1 = Image.open('images/colored.jpg')

    # Aplicar o filtro de Emboss
    # O filtro de emboss cria uma imagem denotando as diferentes regiões como se fossem relevos de diferentes alturas
    # regiões diferentes possuem claramente um relevo diferente umas das outras
    img2 = img1.filter(ImageFilter.EMBOSS)

    # Salvar a imagem resultante
    img2.save('images/embossImage.jpg')

if __name__ == "__main__":
    run()