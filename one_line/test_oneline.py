import unittest
from oneline import*


class MyTestCase(unittest.TestCase):
    def test_probability(self):
        v1 = [(2, 1), (-1, 2), (0, 1), (1, 0), (3, -1), (2, 0), (0, -2), (-2, 1), (1, -3), (0, -1)]
        self.assertEqual(probability(v1,7),10.87)

    def test_amplitudTransicion(self):
        v1 = [(2, 1), (-1, 2), (0, 1), (1, 0), (3, -1), (2, 0), (0, -2), (-2, 1), (1, -3), (0, -1)]
        v2 = [(-1, -4), (2, -3), (-7, 6), (-1, 1), (-5, -3), (5, 0), (5, 8), (4, - 4), (8, -7), (2, -7)]
        self.assertEqual(amplitudTransicion(v1,v2), (-0.02, -0.13))


if __name__ == '__main__':
    unittest.main()
