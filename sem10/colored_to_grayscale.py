from PIL import Image
import sys

# Convertendo uma imagem colorida JPG em uma escala de cinza JPG

# Verificando os argumentos

if __name__ == "__main__":

    # Abrir a imagem
    img = Image.open(sys.argv[1])
    matriz = img.load()

    # Fazer o processamento digital de imagens
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = matriz[i, j][0]
            g = matriz[i, j][1]
            b = matriz[i, j][2]
            pixels = int((r + g + b) / 3)
            matriz[i, j] = (pixels, pixels, pixels)

    # Salvar a imagem
    img.save(sys.argv[2])
