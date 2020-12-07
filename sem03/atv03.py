from PIL import Image

img = Image.open('atv03.png')
print(img.size)
matriz = img.load()

for i in range(13):
    matriz[1,i] = (0,255,25)
    matriz[2,i] = (90,10,90)
    matriz[3,i] = (10,30,200)

img.save('atv03.png')