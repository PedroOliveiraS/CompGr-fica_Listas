from PIL import Image

def run():
    # Abrir a imagem
    img = Image.open('images/imageFromHabitsMrKitty.jpg')

    # Carregar a imagem para uma matriz
    matriz = img.load()

    # Fazer as operações / conversões
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = matriz[i, j][0]
            g = matriz[i, j][1]
            b = matriz[i, j][2]
            p = (int((r + g + b)/3))
            matriz[i,j] = (p, p, p)

    # Salvar a imagem
    img.save('images/ColorToGrayscale.jpg')

if __name__ == "__main__":
    run()