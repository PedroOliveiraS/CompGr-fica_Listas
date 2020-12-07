from PIL import Image

# Abrir a imagem
img = Image.open('../sem04/images/arara.jpg')

# Carregar para uma matriz
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
img.save('images/araraCinza.jpg')