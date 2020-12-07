from PIL import Image

def run():

    #01) Pegue uma imagem colorida qualquer e converta para escala de cinza.
    #
    #

    # Abrir a imagem
    img = Image.open('images/colored.jpg')

    # Carregar a imagem para uma matriz
    matriz = img.load()

    # Fazer a conversão
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = matriz[i,j][0]
            g = matriz[i,j][1]
            b = matriz[i,j][2]
            pixels = int((r + g + b)/3)
            matriz[i,j] = (pixels, pixels, pixels)

    # Salvar a imagem nova
    img.save('images/convertedGrayscale.jpg')

if __name__ == "__main__":
    run()