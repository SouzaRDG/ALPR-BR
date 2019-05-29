from openalpr import Alpr
import re
import cv2
import bdConnection

###### TRABALHANDO COM ViDEOS

# alpr = Alpr("br", "/etc/openalpr/openalpr.conf", "/home/souzardg/openalpr/runtime_data")
# if not alpr.is_loaded():
#     print("Error loading OpenALPR")
#     sys.exit(1)
#
# alpr2 = Alpr("br2", "/etc/openalpr/openalpr.conf", "/home/souzardg/openalpr/runtime_data")
# if not alpr2.is_loaded():
#     print("Error loading OpenALPR")
#     sys.exit(1)
#
# alpr.set_top_n(200)
# alpr2.set_top_n(200)
#
# video = cv2.VideoCapture(0)
# ultimaPlaca = ""
# placa = ''
#
# while (True):
#
#     _, frame = video.read()
#     cv2.imshow('CAM', frame)
#     results = alpr.recognize_ndarray(frame)
#     resultados = alpr2.recognize_ndarray(frame)
#
#     for plate in results['results']:
#
#         for candidate in plate['candidates']:
#
#             if (re.search('^[A-Z]{3}[0-9]{4}', candidate['plate'])):
#                 placa = candidate['plate']
#                 break
#
#         if ((placa != "") & (placa != ultimaPlaca)):
#             ultimaPlaca = placa
#             bdConnection.pesquisaPlaca(placa)
#
#     for plate in resultados['results']:
#
#         for candidate in plate['candidates']:
#
#             if (re.search('^[A-Z]{3}[0-9]{4}', candidate['plate'])):
#                 placa = candidate['plate']
#                 break
#
#         if ((placa != "") & (placa != ultimaPlaca)):
#             ultimaPlaca = placa
#             bdConnection.pesquisaPlaca(placa)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):  #### Aperte 'Q' para fechar
#         cv2.destroyAllWindows()
#         break
#
# video.release()
# alpr.unload()
# alpr2.unload()

##################      TRABALHANDO COM IMAGENS

alpr = Alpr("br2", "/usr/share/openalpr/config/alprd.defaults.conf", "/home/souzardg/openalpr/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(200)


### Selecione o arquivo da imagem
results = alpr.recognize_file("placas/m02.jpg")

### Caso voce queira ver a imagem mude aqui
image = cv2.imread('placas/m02.jpg')
cv2.imshow("imagem", image)

i = 0
placa = ""


for plate in results['results']:

    i += 1
    print("Plate #%d" % i)
    print("   %12s %12s" % ("Plate", "Confidence"))

    for candidate in plate['candidates']:
        prefix = "-"

        print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
        teste = candidate['plate']

        # if( teste[0].isalpha() & teste[1].isalpha() & teste[2].isalpha() & teste[3].isdigit() & teste[4].isdigit() & teste[5].isdigit() & teste[6].isdigit()):
        #     placa = candidate['plate']
        #     confianca = candidate['confidence']
        #     break

        x = re.search('^[A-Z]{3}[0-9]{4}',teste)
        if(x):
            placa = candidate['plate']
            break

if(placa != ""):

    print(placa)
    bdConnection.pesquisaPlaca(placa)



alpr.unload()
cv2.waitKey()
cv2.destroyAllWindows()