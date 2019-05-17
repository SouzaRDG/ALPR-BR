from openalpr import Alpr
import re
import cv2
import bdConnection


alpr = Alpr("br", "/etc/openalpr/openalpr.conf", "/home/souzardg/openalpr/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(200)
# alpr.set_default_region("md")

results = alpr.recognize_file("placas/05.jpg")
image = cv2.imread('placas/05.jpg')
cv2.imshow("pla", image)

i = 0
placa = ""


for plate in results['results']:


    i += 1
    print("Plate #%d" % i)
    print("   %12s %12s" % ("Plate", "Confidence"))
    for candidate in plate['candidates']:
        prefix = "-"
        if candidate['matches_template']:
            prefix = "*"

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

print(placa)

bdConnection.pesquisaPlaca(placa)

# Call when completely done to release memory
alpr.unload()

cv2.waitKey()
cv2.destroyAllWindows()