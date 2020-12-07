from PIL import Image, ImageFilter

# Abrir a imagem
img1 = Image.open('../sem04/images/arara.jpg')

# Criar o kernel
kernel = ImageFilter.Kernel((3,3), (-1,-1,-1,-1,8,-1,-1,-1,-1), 1 , 0)
kernel2 = ImageFilter.Kernel((3,3), (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1),1,0)
# Aplicar o kernel na imagem
img2 = img1.filter(kernel2)

# Salvar a imagem resultante
img2.save('images/araraFiltrada.jpg')