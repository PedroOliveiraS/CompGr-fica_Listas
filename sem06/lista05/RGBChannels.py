from PIL import Image, ImageFilter

def run():

    ############################ CAMADA R
    # Abrir a imagem
    img = Image.open('images/colored.jpg')

    # Carregar a imagem para uma matriz
    matriz = img.load()

    # Realizar as operações da transformação pixel de transformações
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = matriz[i,j][0]
            g = 0 #g = matriz[i,j][1]
            b = 0 #b = matriz[i,j][2]
            matriz[i,j] = (r,g,b)

    img.save('images/camada_r.jpg')

    ############################ CAMADA G
    # Reabrir a imagem
    img = Image.open('images/colored.jpg')

    # Recarregar a imagem para uma matriz
    matriz = img.load()

    # Realizar as operações da transformação pixel de transformações
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = 0 #r = matriz[i,j][0]
            g = matriz[i,j][1]
            b = 0 #b = matriz[i,j][2]
            matriz[i,j] = (r,g,b)

    img.save('images/camada_g.jpg')

    # Reabrir a imagem
    img = Image.open('images/colored.jpg')

    ############################ CAMADA B

    # Recarregar a imagem para uma matriz
    matriz = img.load()

    # Realizar as operações da transformação pixel de transformações
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = 0 #r = matriz[i,j][0]
            g = 0 #g = matriz[i,j][1]
            b = matriz[i,j][2]
            matriz[i,j] = (r,g,b)

    img.save('images/camada_b.jpg')

if __name__ == "__main__":
    run()