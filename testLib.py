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
    def test_sumaVectorial(self):
        v1, v2 = [(3,2),(4,3)], [(1,4),(5,9)]
        self.assertEqual(sumaVectorial(v1,v2),[(4,6),(9,12)])

    def test_inverso(self):
        v1 = [(3,2),(4,3)]
        self.assertEqual(inverso(v1),[(-3,-2),(-4,-3)])

    def test_productoEscalar(self):
        c, v1 = (2,3), [(1,3),(4,2),(4,3)]
        self.assertEqual(productoEscalar(c,v1),[(-7,9), (2,16), (-1,18)])

    def test_sumaMatrices(self):
        m1, m2 = [[(2,1),(4,9)],[(3,5),(7,10)]], [[(-1,5),(6,2)],[(7,-8),(2,3)]]
        self.assertEqual(sumaMatrices(m1,m2),[[(1,6),(10,11)],[(10,-3),(9,13)]])

    def test_inversoMatrices(self):
        m1 = [[(2,1),(4,9)],[(3,5),(7,-10)]]
        self.assertEqual(m1,[[(-2,-1),(-4,-9)],[(-3,-5),(-7,10)]])

    def test_multEscalarMatriz(self):
        c1, m1 = (2,3),[[(2,1),(4,9)],[(3,5),(7,10)]]
        self.assertEqual(multEscalarMatriz(c1,m1),[[(1,8),(-19,30)],[(-9,19),(-16,41)]])

    def test_transpuesta(self):
        m1 = [[(2,1),(4,9)],[(3,5),(7,10)]]
        self.assertEqual(transpuesta(m1),[[(2,1),(3,5)],[(4,9),(7,10)]])

    def test_matrizConjugada(self):
        m1 = [[(2,1),(4,9)],[(3,5),(7,10)]]
        self.assertEqual(matrizConjugada(m1),[[(2,-1),(4,-9)],[(3,-5),(7,-10)]])

    def test_matrizAdjunta(self):
        m1 = [[(-1,5),(6,2)],[(7,-8),(2,3)]]
        self.assertEqual(matrizAdjunta(m1),[[(-1,-5),(7,8)],[(6,-2),(2,-3)]])

if __name__ == '__main__':
    unittest.main()
