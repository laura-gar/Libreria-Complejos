import unittest
from teoriaCuanticaBasica import *


class MyTestCase(unittest.TestCase):
    def test_probability(self):
        v = [(2, 1), (-1, 2), (0, 1), (1, 0), (3, -1), (2, 0), (0, -2), (-2, 1), (1, -3), (0, -1)]
        self.assertEqual(probability(v, 7), 10.87)

    def test_amplitudTransicion(self):
        v = [(2, 1), (-1, 2), (0, 1), (1, 0), (3, -1), (2, 0), (0, -2), (-2, 1), (1, -3), (0, -1)]
        z = [(-1, -4), (2, -3), (-7, 6), (-1, 1), (-5, -3), (5, 0), (5, 8), (4, -4), (8, -7), (2, -7)]
        self.assertEqual(amplitudTransicion(v, z), (-0.02, -0.13))

    def test_media(self):
        m = [[(2, 0), (1, 1)], [(1, -1), (3, 0)]]
        v = [(1 / math.sqrt(2), 0), (0, 1 / math.sqrt(2))]
        self.assertEqual(expectedValue(m, v), 1.5)

    def test_varianza(self):
        m = [[(2, 0), (1, 1)], [(1, -1), (3, 0)]]
        v = [(1 / math.sqrt(2), 0), (0, 1 / math.sqrt(2))]
        self.assertEqual(varianza(m, v), 1.25)

    def test_eigenValues_eigenVectors(self):
        m = [[(2, 0), (1, 1)], [(1, -1), (3, 0)]]
        v = [(1 / math.sqrt(2), 0), (0, 1 / math.sqrt(2))]
        self.assertEqual(reviewObs(m, v), ([1, 4], [(-1, -1), (1, 0)]))

    def test_probabilidadDeTransicion(self):
        m = [[(2, 0), (1, 1)], [(1, -1), (3, 0)]]
        v = [(1 / math.sqrt(2), 0), (0, 1 / math.sqrt(2))]
        self.assertEqual(prob(m, v), (-0.408, -0.0))

    def test_dynamic(self):
        m = [[(0, 0), (1 / math.sqrt(2), 0), (1 / math.sqrt(2), 0), (0, 0)],
             [(0, 1 / math.sqrt(2)), (0, 0), (0, 0), (1 / math.sqrt(2), 0)],
             [(1 / math.sqrt(2), 0), (0, 0), (0, 0), (0, 1 / math.sqrt(2))],
             [(0, 0), (1 / math.sqrt(2), 0), (-1 / math.sqrt(2), 0), (0, 0)]]
        v = [(1, 0), (0, 0), (0, 0), (0, 0)]
        self.assertEqual(dynamic(3, m, v), True)


if __name__ == '__main__':
    unittest.main()
