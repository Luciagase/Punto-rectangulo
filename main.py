'''
Crea una clase llamada Punto con sus dos coordenadas X e Y.
Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:

'''

import math

class Punto: #Clase llamada Punto
    def __init__(self, x=0, y=0):#método constructor para crear puntos fácilmente
        self.x = x
        self.y = y

    def __str__(self): #Imprimir por pantalla un punto
        return "({}, {})".format(self.x, self.y)

    def cuadrante(self):#método llamado cuadrante que indique a qué cuadrante pertenece el punto
        if self.x and self.y > 0:
            print("{} está en el 1º cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} está en el 2º cuadrante".format(self))
        elif self.x and self.y < 0:
            print("{} está en el 3º cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} está en el 4º cuadrante".format(self))
        else:
            print("{} está sobre el origen".format(self))

    def vector(self, punto):#método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos
        print("El vector resultante de {} y {} es ({}, {})".format(self, punto, punto.x - self.x, punto.y - self.y))

    def distancia(self, punto):

