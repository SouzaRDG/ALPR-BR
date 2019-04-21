

###### TENHAM CERTEZA QUE ESTÃO USANDO PYTHON 3



### -------- BIBLIOTECAS --------

import cv2
import PlacasTeste
import pytesseract as ocr
import numpy as np
from PIL import Image


###   AQUI VAMOS POR OS METODOS QULSTME SÃO MAIORES QUE UMA LINHA!
###   ASSIM FICA MAIS LIMPO E FACIL DE IDENTIFICAR O QUE ESTÁ SENDO VIZUALIZADO!!!


def altoCont (imagem):

    structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    imgTopHat = cv2.morphologyEx(imagem, cv2.MORPH_TOPHAT, structuringElement)
    imgBlackHat = cv2.morphologyEx(imagem, cv2.MORPH_BLACKHAT, structuringElement)

    imgGrayscalePlusTopHat = cv2.add(imagem, imgTopHat)
    retorno = cv2.subtract(imgGrayscalePlusTopHat, imgBlackHat)

    return retorno





# image = cv2.imread('placas/cam1.png')
image = cv2.imread('placas/01.jpg')


imgGray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
imgAltoCon = altoCont(imgGray)
imgBlur = cv2.blur(imgAltoCon, (6, 6) )
_ ,imgThresh = cv2.threshold(imgBlur, 110 ,255, cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY_INV)
# _ ,imgThresh = cv2.threshold(imgBlur, 100 ,255, cv2.THRESH_OTSU , cv2.THRESH_BINARY_INV)
# _ ,imgThresh = cv2.threshold(imgBlur, 110 ,255,cv2.THRESH_BINARY_INV,cv2.THRESH_OTSU )
# _ ,imgThresh2 = cv2.threshold(imgThresh, 120 ,255,cv2.THRESH_BINARY_INV, cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_DILATE, ( 3 , 3 ))
imgDilated = cv2.dilate(imgThresh,kernel, iterations = 3)
contours, _ = cv2.findContours(imgDilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.imshow("sss", image)


listaPlacas = list()

for contour in contours:
    [x,y,w,h] = cv2.boundingRect(contour)
    if h>130 and w>130:
         continue
    if h < 80 or w < 80:
        continue
    if w < 2.8 * h:
        continue
    if w > 3.1 * h:
        continue

    cv2.rectangle(imgDilated, (x,y), (x+w,y+h) , 100 , 3)

    imgPossivelPlaca = image[y+35:y+h-18 , x+20:x+w-20]

    imgResize = cv2.resize(imgPossivelPlaca, (0, 0), fx=3, fy=3)

    novaPlaca = PlacasTeste.PlacasTeste(x, y, w, h, imgResize)

    listaPlacas.append(novaPlaca)


for placa in listaPlacas:

    cv2.imwrite(placa.nome + '.png', placa.image)


    placa.image = cv2.cvtColor(placa.image, cv2.COLOR_RGB2GRAY)

    _ , placa.image = cv2.threshold(placa.image, 180 ,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
    cv2.imshow("x", placa.image)

    # those which weren't that small are back but there are less of them
    placa.image = cv2.erode(placa.image, np.ones(( 5 , 4), np.uint8), iterations=5)
    # make small details disapear
    placa.image = cv2.dilate(placa.image, np.ones((4 , 6), np.uint8), iterations=2)


    placa.image = cv2.Canny(placa.image , 230, 255, apertureSize = 3, L2gradient=True)



    # text = ocr.image_to_string(Image.fromarray(placa.image), "mittSemHifen" ,config="-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # text = ' '.join(text.split())

    # print(text + ' ' + placa.nome)


    cv2.imshow(placa.nome,placa.image)


    text = ocr.image_to_string(placa.image, "charplaca")
    print(text + ' ' + placa.nome)

    text = ocr.image_to_string(placa.image, "mittSemHifen")
    print(text + ' ' + placa.nome)

    text = ocr.image_to_string(placa.image, "mittComHifen")
    print(text + ' ' + placa.nome)

    text = ocr.image_to_string(placa.image, "manSemHifen")
    print(text + ' ' + placa.nome)

    text = ocr.image_to_string(placa.image, "manComHifen")
    print(text + ' ' + placa.nome)

    text = ocr.image_to_string(placa.image)
    print(text + ' ' + placa.nome)

    # cv2.imwrite(placa.nome + '.png', placa.image)







# cv2.imshow("image", image)
# cv2.imshow("dilated", imgDilated)

cv2.waitKey()
# cv2.destroyAllWindows()
