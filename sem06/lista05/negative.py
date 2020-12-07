#02) Pegue a mesma imagem original do exercício 01 e aplique o filtro negativo nesta imagem.
#

def run():
    from PIL import Image

    # Abrir a imagem
    img = Image.open('images/colored.jpg')

    # Carregar a imagem para uma matriz
    matriz = img.load()

    # Realizar as operações pixela pixel de transformações
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = 255 - matriz[i,j][0] # retorna uma tupla (r, g, b)
            g = 255 - matriz[i,j][1]
            b = 255 - matriz[i,j][2]
            matriz[i,j] = (r,g,b)

    img.save('images/newNegative.jpg')

if __name__ == "__main__":
    run()