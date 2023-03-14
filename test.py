import unittest
from database import Punto, Rectangulo
from unittest.mock import patch

class TestPunto(unittest.TestCase):

    def test_cuadrante(self):
        punto1 = Punto(3, 5)
        punto2 = Punto(-3, 5)
        punto3 = Punto(-3, -5)
        punto4 = Punto(3, -5)
        punto5 = Punto(0, 0)
        self.assertEqual(punto1.cuadrante(), "El punto (3,5) pertenece al 1º cuadrante")
        self.assertEqual(punto2.cuadrante(), "El punto (-3,5) pertenece al 2º cuadrante")
        self.assertEqual(punto3.cuadrante(), "El punto (-3,-5) pertenece al 3º cuadrante")
        self.assertEqual(punto4.cuadrante(), "El punto (3,-5) pertenece al 4º cuadrante")
        self.assertEqual(punto5.cuadrante(), "El punto (0,0) se encuentra Sobre el origen")

    def test_vector(self):
        punto1 = Punto(3, 5)
        punto2 = Punto(-2, 4)
        self.assertEqual(punto1.vector(punto2), "El vestor es: (-5, -1)")

    def test_distancia(self):
        punto1 = Punto(0, 0)
        punto2 = Punto(3, 4)
        punto3 = Punto(-3, 4)
        punto4 = Punto(3, -4)
        punto5 = Punto(-3, -4)
        self.assertEqual(punto1.distancia(punto2), "La distancia es: 5.0")
        self.assertEqual(punto1.distancia(punto3), "La distancia es: 5.0")
        self.assertEqual(punto1.distancia(punto4), "La distancia es: 5.0")
        self.assertEqual(punto1.distancia(punto5), "La distancia es: 5.0")


class TestRectangulo(unittest.TestCase):
    def test_base(self):
        r = Rectangulo(Punto(0, 0), Punto(5, 10))
        self.assertEqual(r.base(), "La base es: 5")

    def test_altura(self):
        r = Rectangulo(Punto(0, 0), Punto(5, 10))
        self.assertEqual(r.altura(), "La altura es: 10")

    def test_area(self):
        r = Rectangulo(Punto(0, 0), Punto(5, 10))
        self.assertEqual(r.area(), "El área es: 50")

    def test_base_negativa(self):
        r = Rectangulo(Punto(0, 0), Punto(-5, -10))
        self.assertEqual(r.base(), "La base es: 5")

    def test_altura_negativa(self):
        r = Rectangulo(Punto(0, 0), Punto(-5, -10))
        self.assertEqual(r.altura(), "La altura es: 10")

    def test_area_negativa(self):
        r = Rectangulo(Punto(0, 0), Punto(-5, -10))
        self.assertEqual(r.area(), "El área es: 50")

    def test_base_cero(self):
        r = Rectangulo(Punto(0, 0), Punto(0, 10))
        self.assertEqual(r.base(), "La base es: 0")

    def test_altura_cero(self):
        r = Rectangulo(Punto(0, 0), Punto(5, 0))
        self.assertEqual(r.altura(), "La altura es: 0")

    def test_area_cero(self):
        r = Rectangulo(Punto(0, 0), Punto(0, 0))
        self.assertEqual(r.area(), "El área es: 0")

