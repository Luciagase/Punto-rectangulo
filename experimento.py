'''
Experimentación
Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
Consulta a que cuadrante pertenecen el punto A, C y D.
Consulta los vectores AB y BA.
(Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
(Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
Crea un rectángulo utilizando los puntos A y B.
Consulta la base, altura y área del rectángulo.

'''
from database import Punto, Rectangulo

# Crear puntos
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Imprimir puntos
print(A)
print(B)
print(C)
print(D)

# Consultar cuadrante
A.cuadrante()
C.cuadrante()
D.cuadrante()

# Consultar vectores
A.vector(B)
B.vector(A)

# Consultar distancia
A.distancia(B)
B.distancia(A)
print("La distancia entre {} y {} es {}".format(A, B, A.distancia(B)))
print("La distancia entre {} y {} es {}".format(B, A, B.distancia(A)))


# Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
def mas_lejos(distA, distB, distC):
    mayor = max(distA, distB, distC)
    if mayor == distA:
        return A
    elif mayor == distB:
        return B
    else:
        return C

distA = A.distancia(D)
distB = B.distancia(D)
distC = C.distancia(D)

print("El punto más lejos del origen es {}".format(mas_lejos(distA, distB, distC)))

#Crea un rectángulo utilizando los puntos A y B
rectangulo = Rectangulo(A, B)

#Consulta la base, altura y área del rectángulo.
rectangulo.base()
rectangulo.altura()
rectangulo.area()

