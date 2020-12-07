# Importar as bibliotecas
from PIL import Image, ImageFilter

def run():

    # Abrir a Imagem
    img1 = Image.open('images/colored.jpg')

    # Aplicar o filtro de edge enhance more
    # O filtro de edge enhance faz com que as bordas de diferentes regiões estejam presentes de forma muito mais
    # explícita, ficando mais claro a distinção dessas regiões umas das outras (Ainda mais que o edge enhance normal)
    # As bordas chegam quase a brilhar em branco k
    img2 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE)

    # Salvar a imagem resultante
    img2.save('images/edgeEnhanceMoreImage.jpg')

if __name__ == "__main__":
    run()