from PIL import Image

img = Image.open('images/arara.jpg')

# Converter de JPG para PNG
imgpng = img.convert('RGBA')

# Verifica quais bandas a imagem tem
print(img.getbands())
print(imgpng.getbands())

# Obtem uma lista com os pixels da imagem
pixels = list(imgpng.getdata())
print(pixels[0])

# Alterando o valor do canal alpha de todos os pixels
for i, p in enumerate(pixels):
    alpha = 50
    pixels[i] = (p[0], p[1], p[2], alpha)

# Criar uma iamgem nova
outputImg = Image.new('RGBA', img.size)

# Inserir os pixels alterados
outputImg.putdata(pixels)

# Salvar a iamgem nova
outputImg.save('images/imagesAraraAlpha.jpg')