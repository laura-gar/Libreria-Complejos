import unittest
from ComplexLib import*

class MyTestCase(unittest.TestCase):
    def test_sumaComplejos(self):
        a, b = (1, 3), (2, 5)
        self.assertEqual(sumaComplejos(a,b), (3,8))

    def test_productoComplejos(self):
        a, b = (3,-1), (1,4)
        self.assertEqual(productoComplejos(a,b),(7,11))

    def test_restaComplejos(self):
        a, b = (2,3), (3,4)
        self.assertEqual(restaComplejos(a,b),(-1,-1))

    def test_divisionComplejos(self):
        a, b = (0,3), (1,-1)
        self.assertEqual(divisionComplejos(a,b),(-1.5,1.5))

    def test_modulo(self):
        a = (3,1)
        self.assertEqual(modulo(a),3.16)

    def test_conjugado(self):
        a = (3,5)
        self.assertEqual(conjugado(a),(3,-5))

    def test_returnPhase(self):
        a, b, c, d = (1,1), (-1,1), (-1,-1), (1,-1)
        self.assertEqual(returnPhase(a), 0.79)
        self.assertEqual(returnPhase(b), 2.36)
        self.assertEqual(returnPhase(c), 3.93)
        self.assertEqual(returnPhase(d), 5.5)

    def test_cartToPol(self):
        a = (1,1)
        self.assertEqual(cartToPol(a),(1.41,0.79))
        
    def test_sumaVectores(self):
        v1, v2 = [(3,2),(4,3)], [(1,4),(5,9)]
        self.assertEqual(sumaVectores(v1,v2),[(4,6),(9,12)])

    def test_inversoVectores(self):
        v1 = [(3,2),(4,3)]
        self.assertEqual(inversoVectores(v1),[(-3,-2),(-4,-3)])

    def test_escalarPorVector(self):
        c, v1 = (2,3), [(1,3),(4,2),(4,3)]
        self.assertEqual(escalarPorVector(c,v1),[(-7,9), (2,16), (-1,18)])

    def test_sumaMatrices(self):
        m1, m2 = [[(2,1),(4,9)],[(3,5),(7,10)]], [[(-1,5),(6,2)],[(7,-8),(2,3)]]
        self.assertEqual(sumaMatrices(m1,m2),[[(1,6),(10,11)],[(10,-3),(9,13)]])

    def test_inversoMatrices(self):
        m1 = [[(2,1),(4,9)],[(3,-5),(7,-10)]]
        self.assertEqual(inversoMatrices(m1),[[(-2, -1), (-4, -9)], [(-3, 5), (-7, 10)]])

    def test_escalarPorMatriz(self):
        c1, m1 = (2,3), [[(2,1),(4,9)],[(3,-5),(7,10)]]
        self.assertEqual(escalarPorMatriz(c1,m1), [(1, 8), (-19, 30), (21, -1), (-16, 41)])

    def test_transpuesta(self):
        m1 = [[(2,1),(4,9)],[(3,5),(7,10)]]
        self.assertEqual(transpuesta(m1),[[(2,1),(3,5)],[(4,9),(7,10)]])

    def test_matrizConjugada(self):
        m1 = [[(2,1),(4,9)],[(3,5),(7,10)]]
        self.assertEqual(matrizConjugada(m1),[[(2,-1),(4,-9)],[(3,-5),(7,-10)]])

    def test_matrizAdjunta(self):
        m1 = [[(-1,5),(6,2)],[(7,-8),(2,3)]]
        self.assertEqual(matrizAdjunta(m1),[[(-1,-5),(7,8)],[(6,-2),(2,-3)]])

    def test_productoMatrices(self):
        m1, m2 = [[(2,0),(4,0)],[(3,0),(2,0)]], [[(1,0),(2,0),(3,0)],[(4,0),(8,0),(10,0)]]
        self.assertEqual(productoMatrices(m1,m2),[[(18, 0), (36, 0), (46, 0)], [(11, 0), (22, 0), (29, 0)]])

    def test_action(self):
        m1, v1 = [[(2,0),(5,0),(3,0)],[(4,0),(9,0),(2,0)],[(7,0),(1,0),(3,0)]],[[(2,0)],[(4,0)],[(6,0)]]
        self.assertEqual(action(m1,v1),[[(42, 0)], [(56, 0)], [(36, 0)]])

    def test_innerProduct(self):
        v1 = [[(3.5,7.8)],[(4.1,-8.9)]]
        self.assertEqual(innerProduct(v1, v1), 169.11)

    def test_norma(self):
        v1 = [[(3.5,7.8)],[(4.1,-8.9)]]
        self.assertEqual(norma(v1),13.0)

    def test_distanciaVectores(self):
        v1, v2 = [[(3,0)],[(1,0)],[(2,0)]], [[(2,0)],[(2,0)],[(-1,0)]]
        self.assertEqual(distanciaVectores(v1,v2),3.32)

    def test_matrizUnitary(self):
        m1 = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
        self.assertEqual(matrizUnitary(m1), True)

    def test_matrizHermitain(self):
        m1 = [[(7,0),(6,5)],[(6,-5),(-3,0)]]
        self.assertEqual(matrizHermitiana(m1),True)

    def test_prodTensor(self):
        v1, v2 = [[(2,0)], [(3, 0)]], [[(4, 0)], [(6, 0)], [(3, 0)]]
        self.assertEqual(productoTensor(v1,v2),[[(8, 0)], [(12, 0)], [(6, 0)], [(12, 0)], [(18, 0)], [(9, 0)]])
if __name__ == '__main__':
    unittest.main()
