# Importar o módulo Image do PIL
from PIL import Image

# Abrir uma imagem existente
imageOriginal = Image.open('images/arara.jpg')

# Fazer a rotação Image.FLIP_LEFT_RIGHT
imageEspelhada = imageOriginal.transpose(Image.FLIP_LEFT_RIGHT)

# Mostrar a imagem original
#imageOriginal.show()

# Mostrar a imagem espelhada
#imageEspelhada.show()

# Salvar a imagem espelhada
imageEspelhada.save('images/araraEspelhadaHorizontal.jpg')