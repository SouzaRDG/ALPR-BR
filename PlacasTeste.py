#Classe para por as possiveis placas à serem testadas


class PlacasTeste:

    numPlacas = 0

    def __init__(self, x, y, w, h, image):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.nome = f'Placa{PlacasTeste.numPlacas + 1}'
        self.image = image

        PlacasTeste.numPlacas +=1


    # def novaPlaca(self, x, y, w, h, image):
    #
    #     novaPlaca = PlacasTeste()
    #     self.x = x
    #     self.y = y
    #     self.w = w
    #     self.h = h
    #     self.nome = f'Placa {PlacasTeste.numPlacas + 1}'
    #     self.image = image
    #
    #     PlacasTeste.numPlacas +=1
    #
    #     return novaPlaca