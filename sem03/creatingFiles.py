from PIL import Image

# Imagem 01
mode = 'RGB'
size = (11,12) #Coluna / Linha
color = (255,255,255)
img = Image.new(mode,size,color)
matriz = img.load()

for i in range(7):
    matriz[(i+2),3] = (0,0,0)
    matriz[(i+2),10] = (0,0,0)

for i in range(8):
    matriz[8,(i+3)] = (0,0,0)
    matriz[2,(i+3)] = (0,0,0)

for i in range(5):
    matriz[(i+3),2] = (0,0,0)

for i in range(3):
    matriz[(i+4),1] = (0,0,0)

matriz[5,0] = (0,0,0)
img.save('atv01.png')

# IMAGEM 02
size = (4, 8)
color = (0,0,0)
img = Image.new(mode,size,color)
matriz = img.load()

for i in range(6):
    matriz[1,(1+i)] = (200,200,200)
    matriz[2,(1+i)] = (120,120,120)
    matriz[3,(1+i)] = (88,88,88)

img.save('atv02.png')

# IMAGEM 03
size = (4, 13)
color = (255,0,25)
img = Image.new(mode,size,color)
matriz = img.load()

for i in range(13):
    matriz[1,i] = (0,255,25)
    matriz[2,i] = (90,10,90)
    matriz[3,i] = (10,30,200)

img.save('atv03.png')