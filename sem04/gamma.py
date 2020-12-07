# Transformação gamma
from  PIL import Image

# Abrir a imagem
img = Image.open('images/panda.jpg')

# Carregar a imagem para uma matriz
matriz = img.load()

# Realizar as operçaões píxel a píxel da transformação
gamma = 2.0

for i in range(img.size[0]):
    for j in range (img.size[1]):
        r = int((matriz[i,j][0]/255) ** gamma * 255)
        g = int((matriz[i,j][1]/255) ** gamma * 255)
        b = int((matriz[i,j][2]/255) ** gamma * 255)
        matriz[i,j] = (r,g,b)

# Salvar a imagem
img.save('images/gammaPanda2.jpg')