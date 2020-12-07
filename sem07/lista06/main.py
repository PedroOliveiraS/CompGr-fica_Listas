#Imports

from sem07.lista06 import blurImage
from sem07.lista06 import contourImage
from sem07.lista06 import detailImage
from sem07.lista06 import edgeEnhanceImage
from sem07.lista06 import edgeEnhanceMoreImage
from sem07.lista06 import embossImage
from sem07.lista06 import findEdgesImage
from sem07.lista06 import sharpenImage
from sem07.lista06 import smoothImage
from sem07.lista06 import smoothMoreImage

def runBlur():
    # Esse filtro aplica um efeito de embaçamento / enevoamento na imagem
    blurImage.run()

def runContour():

    # A aplicação desse filtro resulta em uma imagem preto e branco, destacando os contornos entre os objetos
    # / personagens presentes na imagem
    contourImage.run()

def runDetail():
    # A aplicação desse filtro melhora os detalhes e cores da imagem, dando uma maior nitidez a diferentes áreas
    detailImage.run()

def runEdgeEnhance():
    # O filtro de edge enhance faz com que as bordas de diferentes regiões estejam presentes de forma muito mais
    # explícita, ficando mais claro a distinção dessas regiões umas das outras
    edgeEnhanceImage.run()

def runEdgeEnhanceMore():
    # O filtro de edge enhance faz com que as bordas de diferentes regiões estejam presentes de forma muito mais
    # explícita, ficando mais claro a distinção dessas regiões umas das outras (Ainda mais que o edge enhance normal)
    # As bordas chegam quase a brilhar em branco k
    edgeEnhanceMoreImage.run()

def runEmboss():
    # O filtro de emboss cria uma imagem denotando as diferentes regiões como se fossem relevos de diferentes alturas
    # regiões diferentes possuem claramente um relevo diferente umas das outras
    embossImage.run()

def runFindEdge():
    # Esse filtro tem como objetivo denotar as bordas das regiões presentes na imagem
    findEdgesImage.run()

def runSharpen():
    # O filtro de sharpen aumenta a nitidez das regiões presentes em uma imagem
    sharpenImage.run()

def runSmooth():
    # O filtro aplica uma redução de nitidez nas bordas das diferentes regiões presentes na imagem
    smoothImage.run()

def runSmoothMore():
    # O filtro aplica uma redução ainda maior de nitidez nas bordas das diferentes regiões presentes na imagem
    smoothMoreImage.run()

if __name__ == "__main__":
    runBlur()
    runContour()
    runDetail()
    runEdgeEnhance()
    runEdgeEnhanceMore()
    runEmboss()
    runFindEdge()
    runSharpen()
    runSmooth()
    runSmoothMore()