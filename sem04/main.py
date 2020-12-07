# Filtro negativo
from PIL import Image

# Abrir a imagem
img = Image.open('images/panda.jpg')
print(img.size)

# Carregar a imagem para uma matriz
matriz = img.load()

# Realizar as operações pixela pixel de transformações
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = 255 - matriz[i,j][0] # retorna uma tupla (218, 150, 149)
        g = 255 - matriz[i,j][1]
        b = 255 - matriz[i,j][2]
        matriz[i,j] = (r,g,b)

img.save('images/novoPanda.jpg')