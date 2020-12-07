# O que significa a correção gama de uma imagem? Responda como comentário no início do seu código.
# A correção gama de uma imagem se refere a alterar o brilho da mesma, tornando-a mais clara ou mais escura,
# dependendo do que for proposto e necessitado

from PIL import Image

# ----------------------------------Filtro gamma - Questão 2 - Letra A ------------------------------------------
# Abrir a imagem
img = Image.open('images/grayscale.jpg')

# Carregar a imagem para uma matriz
matriz = img.load()
gamma = [0.25, 0.5, 1, 2, 3]

# Realizar as operações pixela pixel de transformações
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int((matriz[i, j][0] / 255) ** gamma[0] * 255)
        matriz[i,j] = (r,r,r)

img.save('images/questao2/letra-a/novoGrayscaleGamma0ponto25.jpg')

# Realizar as operações pixela pixel de transformações
img = Image.open('images/grayscale.jpg') # Reabrindo a imagem
matriz = img.load() # Recarregando a imagem
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int((matriz[i, j][0] / 255) ** gamma[1] * 255)
        matriz[i,j] = (r,r,r)

img.save('images/questao2/letra-a/novoGrayscaleGamma0ponto5.jpg')

# Realizar as operações pixela pixel de transformações
img = Image.open('images/grayscale.jpg') # Reabrindo a imagem
matriz = img.load() # Recarregando a imagem
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int((matriz[i, j][0] / 255) ** gamma[2] * 255)
        matriz[i,j] = (r,r,r)

img.save('images/questao2/letra-a/novoGrayscaleGamma1.jpg')

# Realizar as operações pixela pixel de transformações
img = Image.open('images/grayscale.jpg') # Reabrindo a imagem
matriz = img.load() # Recarregando a imagem
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int((matriz[i, j][0] / 255) ** gamma[3] * 255)
        matriz[i,j] = (r,r,r)

img.save('images/questao2/letra-a/novoGrayscaleGamma2.jpg')

# Realizar as operações pixela pixel de transformações
img = Image.open('images/grayscale.jpg') # Reabrindo a imagem
matriz = img.load() # Recarregando a imagem
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int((matriz[i, j][0] / 255) ** gamma[4] * 255)
        matriz[i,j] = (r,r,r)

img.save('images/questao2/letra-a/novoGrayscaleGamma3.jpg')

# ----------------------------------Filtro gamma - Questão 2 - Letra B ------------------------------------------
# Abrir a imagem
img = Image.open('images/rainbow.jpg')

# Carregar a imagem para uma matriz
matriz = img.load()
gamma = [0.25, 0.5, 1, 2, 3]

# Realizar as operações pixela pixel de transformações
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int((matriz[i, j][0] / 255) ** gamma[0] * 255)
        g = int((matriz[i, j][1] / 255) ** gamma[0] * 255)
        b = int((matriz[i, j][2] / 255) ** gamma[0] * 255)
        matriz[i,j] = (r,g,b)

img.save('images/questao2/letra-b/novoRainbowGamma0ponto25.jpg')

# Realizar as operações pixela pixel de transformações
img = Image.open('images/rainbow.jpg') # Reabrindo a imagem
matriz = img.load() # Recarregando a imagem
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int((matriz[i, j][0] / 255) ** gamma[1] * 255)
        g = int((matriz[i, j][1] / 255) ** gamma[1] * 255)
        b = int((matriz[i, j][2] / 255) ** gamma[1] * 255)
        matriz[i, j] = (r, g, b)

img.save('images/questao2/letra-b/novoRainbowGamma0ponto5.jpg')

# Realizar as operações pixela pixel de transformações
img = Image.open('images/rainbow.jpg') # Reabrindo a imagem
matriz = img.load() # Recarregando a imagem
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int((matriz[i, j][0] / 255) ** gamma[2] * 255)
        g = int((matriz[i, j][1] / 255) ** gamma[2] * 255)
        b = int((matriz[i, j][2] / 255) ** gamma[2] * 255)
        matriz[i, j] = (r, g, b)

img.save('images/questao2/letra-b/novoRainbowGamma1.jpg')

# Realizar as operações pixela pixel de transformações
img = Image.open('images/rainbow.jpg') # Reabrindo a imagem
matriz = img.load() # Recarregando a imagem
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int((matriz[i, j][0] / 255) ** gamma[3] * 255)
        g = int((matriz[i, j][1] / 255) ** gamma[3] * 255)
        b = int((matriz[i, j][2] / 255) ** gamma[3] * 255)
        matriz[i, j] = (r, g, b)

img.save('images/questao2/letra-b/novoRainbowGamma2.jpg')

# Realizar as operações pixela pixel de transformações
img = Image.open('images/rainbow.jpg') # Reabrindo a imagem
matriz = img.load() # Recarregando a imagem
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int((matriz[i, j][0] / 255) ** gamma[4] * 255)
        g = int((matriz[i, j][1] / 255) ** gamma[4] * 255)
        b = int((matriz[i, j][2] / 255) ** gamma[4] * 255)
        matriz[i, j] = (r, g, b)

img.save('images/questao2/letra-b/novoRainbowGamma3.jpg')
