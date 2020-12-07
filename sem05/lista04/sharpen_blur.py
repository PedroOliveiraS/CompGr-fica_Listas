from PIL import  Image, ImageFilter

def run():
    # Abrir a Imagem
    img1 = Image.open('images/originalNature.jpg')

    # Criar o Kernel (Sharpen)
    kernelS = ImageFilter.Kernel((3, 3), (0, -1, 0, -1, 5, -1, 0, -1, 0), 1, 0)

    # Aplicar o filtro na imagem
    img2 = img1.filter(kernelS)

    # Criar o Kernel (Blur
    kernelB  = ImageFilter.Kernel((3, 3), ((1/9), (1/9), (1/9), (1/9), (1/9), (1/9), (1/9), (1/9), (1/9)), 1, 0)

    # Aplicar o filtro na imagem
    img3 = img2.filter(kernelB)

    # Salvar as imagens
    img2.save('images/filtro_sharpen.jpg')
    img3.save('images/filtro_sharpen_mediana.jpg')
if __name__ == "__main__":
    run()