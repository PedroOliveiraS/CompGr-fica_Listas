from PIL import ImageFilter, Image

def filtro03():
    # Abrir a Imagem
    img1 = Image.open('images/originalFachada.jpg')

    # Criar o Kernel
    kernel = ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1, 0)

    # Aplicar o filtro na imagem
    img2 = img1.filter(kernel)

    # Salvar a imagem
    img2.save('images/filtro_3.jpg')

if __name__ == "__main__":
    filtro03()