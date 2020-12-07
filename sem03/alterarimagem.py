from PIL import Image

#Abrir a imagem
img = Image.open('imagemNova.png')

#Dimensões da imagem

print(img.size)
#Carregar a imagem para uma matriz
matriz = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        #print(matriz[i,j], end='') 
        #print(" ",end='')
        pass
    #print()

#Alterando pixels da imagem
#matriz[0,0] = (20, 227, 69)
#matriz[5,2] = (120, 14, 227)
#Salvar a imagem
#img.save('imagemNovaAlterada.png')
#print(matriz)