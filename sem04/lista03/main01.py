# O que significa o negativo de uma imagem? Responda como comentário no início do seu código.
# O negativo de uma imagem significa a cor (em termos numéricos, píxels) proporcionalmente inversa
# a cor (pixel) em questão da imagem original

# Filtro negativo
from PIL import Image

# IMAGEM COLORIDA ---------------------------------------------------------------------------- (A)
# Abrir a imagem
img = Image.open('images/rainbow.jpg')
print(img.size)

# Carregar a imagem para uma matriz
matriz = img.load()

# Realizar as operações pixela pixel de transformações
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = 255 - matriz[i,j][0] # retorna uma tupla (r, g, b)
        g = 255 - matriz[i,j][1]
        b = 255 - matriz[i,j][2]
        matriz[i,j] = (r,g,b)

img.save('images/questao1/novoRainbow.jpg')

# Imagem em escala de cinza ----------------------------------------------------------------- (B)
# Uma iamgem em tom de cinza, no formato rgb, é uma imagem em que os três canais (r,g,b) apresentam o mesmo valor

# Abrir a imagem
img = Image.open('images/grayscale.jpg')

# Carregar a imagem para uma matriz
matriz = img.load()

# Realizar as operações pixel a pixel de transformações
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = 255 - matriz[i,j][0] # retorna uma tupla (218, 150, 149)
        matriz[i,j] = (r,r,r)

img.save('images/questao1/novoGrayscale.jpg')