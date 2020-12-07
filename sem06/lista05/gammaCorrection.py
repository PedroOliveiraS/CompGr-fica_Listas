#Pegue a mesma imagem original do exercício 01 e aplique a correção gamma nesta
# imagem com gamma 1.8, e gamma 0.3. Serão dois arquivos: gamma_1p8, gamma0p3.
def run():
    from PIL import Image

    # Abrir a imagem
    img = Image.open('images/colored.jpg')

    # Carregar a imagem para uma matriz
    matriz = img.load()

    # Realizar as operçaões píxel a píxel da transformação
    gamma = 1.8

    for i in range(img.size[0]):
        for j in range (img.size[1]):
            r = int((matriz[i,j][0]/255) ** gamma * 255)
            g = int((matriz[i,j][1]/255) ** gamma * 255)
            b = int((matriz[i,j][2]/255) ** gamma * 255)
            matriz[i,j] = (r,g,b)

    # Salvar a imagem
    img.save('images/gamma_1p8.jpg')

    # Reabrir a imagem
    img = Image.open('images/colored.jpg')

    # Recarregar a imagem para uma matriz
    matriz = img.load()

    # Realizar as operçaões píxel a píxel da transformação
    gamma = 0.3

    for i in range(img.size[0]):
        for j in range (img.size[1]):
            r = int((matriz[i,j][0]/255) ** gamma * 255)
            g = int((matriz[i,j][1]/255) ** gamma * 255)
            b = int((matriz[i,j][2]/255) ** gamma * 255)
            matriz[i,j] = (r,g,b)

    # Salvar a imagem
    img.save('images/gamma_0p3.jpg')

if __name__ == "__main__":
    run()