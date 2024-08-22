import Libcplx as lc
import unittest
import math

class TestCplxOperations(unittest.TestCase):

    def test_cplx_sum(self):
        a = (3, 2)
        b = (1, 7)
        resultado = lc.cplx_sum(a, b)
        expected = (4, 9)
        self.assertEqual(resultado, expected)

        a = (-1, 5)
        b = (4, -3)
        resultado = lc.cplx_sum(a, b)
        expected = (3, 2)
        self.assertEqual(resultado, expected)

    def test_cplx_sub(self):

        a = (5, 4)
        b = (2, 3)
        resultado = lc.cplx_sub(a, b)
        expected = (3, 1)
        self.assertEqual(resultado, expected)

        a = (1, 1)
        b = (-1, -1)
        resultado = lc.cplx_sub(a, b)
        expected = (2, 2)
        self.assertEqual(resultado, expected)

    def test_cplx_product(self):

        a = (2, 3)
        b = (4, 5)
        resultado = lc.cplx_product(a, b)
        expected = (-7, 22)
        self.assertEqual(resultado, expected)


        a = (0, 1)
        b = (0, 1)
        resultado = lc.cplx_product(a, b)
        expected = (-1, 0)
        self.assertEqual(resultado, expected)

    def test_cplx_modulo(self):

        num = (3, 4)
        resultado = lc.cplx_modulo(num)
        expected = 5.0
        self.assertAlmostEqual(resultado, expected)


        num = (1, 1)
        resultado = lc.cplx_modulo(num)
        expected = math.sqrt(2)
        self.assertAlmostEqual(resultado, expected)

    def test_cplx_div(self):

        a = (4, 2)
        b = (2, -2)
        resultado = lc.cplx_div(a, b)
        expected = (0.0, 1.5)
        self.assertAlmostEqual(resultado[0], expected[0])
        self.assertAlmostEqual(resultado[1], expected[1])


        a = (1, 2)
        b = (1, 1)
        resultado = lc.cplx_div(a, b)
        expected = (1.5, 0.5)
        self.assertAlmostEqual(resultado[0], expected[0])
        self.assertAlmostEqual(resultado[1], expected[1])

    def test_cplx_conjugate(self):

        num = (3, 4)
        resultado = lc.cplx_conjugate(num)
        expected = (3, -4)
        self.assertEqual(resultado, expected)


        num = (-5, -6)
        resultado = lc.cplx_conjugate(num)
        expected = (-5, 6)
        self.assertEqual(resultado, expected)

    def test_cplx_phase(self):

        num = (1, 1)
        resultado = lc.cplx_phase(num)
        expected = math.pi / 4
        self.assertAlmostEqual(resultado, expected)


        num = (-1, 0)
        resultado = lc.cplx_phase(num)
        expected = math.pi
        self.assertAlmostEqual(resultado, expected)

    def test_cplx_convert_cartesian_to_polar(self):

        num = (1, 1)
        resultado = lc.cplx_convert(num, 1)
        expected = (math.sqrt(2), math.pi / 4)
        self.assertAlmostEqual(resultado[0], expected[0])
        self.assertAlmostEqual(resultado[1], expected[1])


        num = (0, 2)
        resultado = lc.cplx_convert(num, 1)
        expected = (2.0, math.pi / 2)
        self.assertAlmostEqual(resultado[0], expected[0])
        self.assertAlmostEqual(resultado[1], expected[1])

    def test_cplx_convert_polar_to_cartesian(self):

        num = (2, math.pi / 2)
        resultado = lc.cplx_convert(num, 2)
        expected = (0.0, 2.0)
        self.assertAlmostEqual(resultado[0], expected[0])
        self.assertAlmostEqual(resultado[1], expected[1])


        num = (1, math.pi)
        resultado = lc.cplx_convert(num, 2)
        expected = (-1.0, 0.0)
        self.assertAlmostEqual(resultado[0], expected[0])
        self.assertAlmostEqual(resultado[1], expected[1])

if __name__ == '__main__':
    unittest.main()
