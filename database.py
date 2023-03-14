'''
Crea una clase llamada Punto con sus dos coordenadas X e Y.
Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:

Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añade al rectángulo un método llamado base que muestre la base.
Añade al rectángulo un método llamado altura que muestre la altura.
Añade al rectángulo un método llamado area que muestre el area.
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

    def distancia(self, punto):#método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla
        dist= math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
        return dist


class Rectangulo:#clase llamada Rectangulo
    def __init__(self, pinicial=Punto(), pfinal=Punto()):#método constructor para crear ambos puntos fácilmente
        self.pinicial = pinicial
        self.pfinal = pfinal

    def base(self):#método llamado base que muestre la base
        self.base = abs(self.pfinal.x - self.pinicial.x)
        print("La base del rectángulo es {}".format(self.base))

    def altura(self):#método llamado altura que muestre la altura
        self.altura = abs(self.pfinal.y - self.pinicial.y)
        print("La altura del rectángulo es {}".format(self.altura))

    def area(self):#método llamado area que muestre el area.
        self.area = self.base * self.altura
        print("El área del rectángulo es {} m^2".format(self.area))