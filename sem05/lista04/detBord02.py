from PIL import ImageFilter, Image

def filtro02():
    # Abrir a Imagem
    img1 = Image.open('images/originalFachada.jpg')

    # Criar o Kernel
    kernel = ImageFilter.Kernel((3, 3), (0, 1, 0, 1, -4, 1, 0, 1, 0), 1, 0)

    # Aplicar o filtro na imagem
    img2 = img1.filter(kernel)

    # Salvar a imagem
    img2.save('images/filtro_2.jpg')

if __name__ == "__main__":
    filtro02()