from PIL import Image

img = Image.open('atv02.png')
print(img.size)
matriz= img.load()

for i in range(6):
    matriz[1,(1+i)] = (200,200,200)
    matriz[2,(1+i)] = (120,120,120)
    matriz[3,(1+i)] = (88,88,88)

img.save('atv02.png')