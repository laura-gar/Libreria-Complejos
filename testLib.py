import unittest
from ComplexLib import*

class MyTestCase(unittest.TestCase):
    def test_suma(self):
        a, b = (1, 3), (2, 5)
        self.assertEqual(suma(a,b), (3,8))

    def test_resta(self):
        a, b = (2,3), (3,4)
        self.assertEqual(resta(a,b),(-1,1))

    def test_multiplicacion(self):
        a, b = (3,-1), (1,4)
        self.assertEqual(multiplicacion(a,b),(7,11))

    def test_division(self):
        a, b = (0,3), (1,-1)
        self.assertEqual(division(a,b),(-1.5,1.5))

    def test_modulo(self):
        a = (3,1)
        self.assertEqual(modulo(a),3.16)

    def test_conjugado(self):
        a = (3,5)
        self.assertEqual(conjugado(a),(3,-5))

    def test_returnPhase(self):
        a, b, c, d = (1,1), (-1,1), (-1,-1), (1,-1)
        self.assertEqual(returnPhase(a), 45.0)
        self.assertEqual(returnPhase(b), 135.0)
        self.assertEqual(returnPhase(c), 225.0)
        self.assertEqual(returnPhase(d), -45.0)

    def test_cartToPol(self):
        a = (1,1)
        self.assertEqual(cartToPol(a),(1.41,-45.0))

if __name__ == '__main__':
    unittest.main()
