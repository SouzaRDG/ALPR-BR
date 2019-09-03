from openalpr import Alpr
import re
import cv2
import bdConnection

###### TRABALHANDO COM ViDEOS

try:
    alpr = Alpr("br", "/etc/openalpr/openalpr.conf", "/home/souzardg/openalpr/runtime_data")
    alpr2 = Alpr("br2", "/etc/openalpr/openalpr.conf", "/home/souzardg/openalpr/runtime_data")
except:
    print("Erro ao carregar OpenALPR\n"
          "Verifique se todos os componentes estão instalados\n")
    exit()

alpr.set_top_n(200)
alpr2.set_top_n(200)
video = cv2.VideoCapture(0)
ultimaPlaca = ""
placa = ""

placeHolder = ""
placaTeste1 = ""
placaTeste2 = ""
placaTeste3 = ""

while (True):

    _, frame = video.read()
    cv2.imshow('CAM', frame)

    results = alpr.recognize_ndarray(frame)
    for plate in results['results']:
        for candidate in plate['candidates']:
            if (re.search('^[A-Z]{3}[0-9]{4}', candidate['plate'])):
                placeHolder = candidate['plate']
                break
    resultados = alpr2.recognize_ndarray(frame)
    for plate in resultados['results']:
        for candidate in plate['candidates']:
            if re.search('^[A-Z]{3}[0-9]{4}', re.sub('[\W_]+', '', candidate['plate'])):
                placeHolder = re.sub('[\W_]+', '', candidate['plate'])
                break

    if(placeHolder != ""):
        if(placaTeste1 == ""):
            placaTeste1 = placeHolder
            placeHolder = ""
        elif(placaTeste2 == ""):
            placaTeste2 = placeHolder
            placeHolder = ""
        elif(placaTeste3 == ""):
            placaTeste3 = placeHolder
            placeHolder = ""
    else:
        placaTeste1 = ""
        placaTeste2 = ""
        placaTeste3 = ""
        placeHolder = ""

    if((placaTeste1 != "") & ((placaTeste1 == placaTeste2) | (placaTeste1 == placaTeste3))):
        placa = placaTeste1
        placeHolder = ""

    if((placaTeste2 != "") & (placaTeste2 == placaTeste3)):
        placa = placaTeste2
        placeHolder = ""


    if ((placa != "") & (placa != ultimaPlaca)):
        ultimaPlaca = placa
        placaTeste1 = ""
        placaTeste2 = ""
        placaTeste3 = ""
        bdConnection.pesquisaPlaca(placa)
        placa = ""

    if cv2.waitKey(1) & 0xFF == ord('q'):  #### Aperte 'Q' para fechar
        cv2.destroyAllWindows()
        break

video.release()
alpr.unload()
alpr2.unload()

##################      TRABALHANDO COM IMAGENS  / Testes

# alpr = Alpr("br", "/usr/share/openalpr/config/alprd.defaults.conf", "/home/souzardg/openalpr/runtime_data")
# if not alpr.is_loaded():
#     print("Error loading OpenALPR")
#     sys.exit(1)
#
# alpr.set_top_n(200)
#
#
# ### Selecione o arquivo da imagem
# results = alpr.recognize_file("placas/00.jpg")
#
# ### Caso voce queira ver a imagem mude aqui
# image = cv2.imread('placas/00.jpg')
# image = cv2.resize(image, (960, 540))                    # Resize image
# cv2.imshow("imagem", image)
# i = 0
# placa = ""
#
#
# for plate in results['results']:
#
#     i += 1
#     print("Plate #%d" % i)
#     print("   %12s %12s" % ("Plate", "Confidence"))
#
#     for candidate in plate['candidates']:
#         prefix = "-"
#
#         print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
#         teste = candidate['plate']
#
#         # if( teste[0].isalpha() & teste[1].isalpha() & teste[2].isalpha() & teste[3].isdigit() & teste[4].isdigit() & teste[5].isdigit() & teste[6].isdigit()):
#         #     placa = candidate['plate']
#         #     confianca = candidate['confidence']
#         #     break
#
#         # x = re.search('^[A-Z]{3}[0-9]{4}',teste) #carro
#         # if(x):
#         #     placa = candidate['plate']
#         #     break
#
#         print(re.sub('[\W_]+', '', candidate['plate'])) #teste para moto (retirando o \n entre as linhas)
#
#         x = re.search('^[A-Z]{3}[0-9]{4}', re.sub('[\W_]+', '', candidate['plate']))  #moto
#         if (x):
#             placa = re.sub('[\W_]+', '', candidate['plate'])
#             break
#
# if(placa != ""):
#
#     print(placa)
#     bdConnection.pesquisaPlaca(placa)
#
#
#
# alpr.unload()
# cv2.waitKey()
# cv2.destroyAllWindows()