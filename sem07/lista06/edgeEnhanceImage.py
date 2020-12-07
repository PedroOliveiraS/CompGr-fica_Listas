# Importar as bibliotecas
from PIL import Image, ImageFilter

def run():

    # Abrir a Imagem
    img1 = Image.open('images/colored.jpg')

    # Aplicar o filtro de Edge Enhance
    # O filtro de edge enhance faz com que as bordas de diferentes regiões estejam presentes de forma muito mais
    # explícita, ficando mais claro a distinção dessas regiões umas das outras
    img2 = img1.filter(ImageFilter.EDGE_ENHANCE)

    # Salvar a imagem resultante
    img2.save('images/edgeEnhanceImage.jpg')

if __name__ == "__main__":
    run()