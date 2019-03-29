

###### TENHAM CERTEZA QUE ESTÃO USANDO PYTHON 3 OU MAIOR



### -------- BIBLIOTECAS --------

import cv2
import PlacasTeste
import pytesseract as ocr
import numpy as np
from PIL import Image


###   AQUI VAMOS POR OS METODOS QUE SÃO MAIORES QUE UMA LINHA!
###   ASSIM FICA MAIS LIMPO E FACIL DE IDENTIFICAR O QUE ESTÁ SENDO VIZUALIZADO!!!


def altoCont (imagem):

    structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    imgTopHat = cv2.morphologyEx(imagem, cv2.MORPH_TOPHAT, structuringElement)
    imgBlackHat = cv2.morphologyEx(imagem, cv2.MORPH_BLACKHAT, structuringElement)

    imgGrayscalePlusTopHat = cv2.add(imagem, imgTopHat)
    retorno = cv2.subtract(imgGrayscalePlusTopHat, imgBlackHat)

    return retorno





# image = cv2.imread('placas/cam1.png')
image = cv2.imread('placas/images/01.jpg')


imgGray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
imgAltoCon = altoCont(imgGray)
imgBlur = cv2.blur(imgAltoCon, (7, 7) )
# _ ,imgThresh = cv2.threshold(imgAltoCon, 135 ,255,cv2.THRESH_BINARY_INV,cv2.THRESH_OTSU )
_ ,imgThresh = cv2.threshold(imgBlur, 110 ,255,cv2.THRESH_BINARY_INV,cv2.THRESH_OTSU )
_ ,imgThresh2 = cv2.threshold(imgThresh, 180 ,255,cv2.THRESH_BINARY, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, ( 3 , 3 ))
imgDilated = cv2.dilate(imgThresh,kernel, iterations = 3)
contours, _ = cv2.findContours(imgDilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


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

    cv2.rectangle(imgDilated,(x,y),(x+w,y+h),(150,0,155),3)

    imgPossivelPlaca = imgDilated[y:y+h,x:x+w]

    imgResize = cv2.resize(imgPossivelPlaca, (0, 0), fx=3, fy=3)

    novaPlaca = PlacasTeste.PlacasTeste(x, y, w, h, imgResize)

    listaPlacas.append(novaPlaca)

for placa in listaPlacas:

    # cv2.imshow(placa.nome,placa.image)

    # make small details dissapear
    result = cv2.dilate(placa.image, np.ones((5, 5), np.uint8), iterations=1)
    # those which weren't that small are back but there are less of them
    result = cv2.erode(result, np.ones((5, 5), np.uint8), iterations=2)

    result = cv2.Canny(result, 80, 255, apertureSize=3, L2gradient=True)









    #
    # text = ocr.image_to_string(Image.fromarray(result), config="-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # text = ' '.join(text.split())


    cv2.imshow(placa.nome,result)

    # cv2.imwrite(placa.nome + '.png', placa.image)

    text = ocr.image_to_string(result)

    print(text + ' ' + placa.nome)






# cv2.imshow("image", image)
# # #cv2.imshow("gray",gray)
# # #cv2.imshow("thresh", thresh)
cv2.imshow("dilated", imgDilated)

cv2.waitKey()
# cv2.destroyAllWindows()
