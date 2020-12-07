from PIL import Image

img = Image.open('atv01.png')
print(img.size)
matriz= img.load()

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