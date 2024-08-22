import Librcomplex as lc
import unittest

class TestComplexOperations(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(lc.sumComple((1,-3),(5,4)), (6,1))
        self.assertAlmostEqual(lc.sumComple((-1.5,4),(-2.4,-10)), (-3.9,-6))

    def test_resta (self):
        self.assertEqual(lc.resComple((1,-5),(2,1)), (-1,-6))
        self.assertAlmostEqual(lc.resComple((5,1.8),(4.5,3)), (0.5,-1.2))
    
    def test_multiplicacion (self):
        self.assertEqual(lc.multiComple((5,-3),(4,1)), (23,-7))
        self.assertAlmostEqual(lc.multiComple((1.5,-1),(0.5,0.5)), (1.25,0.25))
    
    def test_division (self):
        self.assertAlmostEqual(lc.diviComple((-4,-7),(1,3)), (-2.5,0.5))
        self.assertAlmostEqual(lc.diviComple((3.5,-1),(4,-2)), (0.8, 0.15))

    def test_modulo (self):
        self.assertEqual(lc.modulComple((3,4)), 5)
        self.assertAlmostEqual(lc.modulComple((2,9)), 9.219544457)
    
    def test_conjugado (self):
        self.assertEqual(lc.conjugado((3,5)), (3,-5))
        self.assertEqual(lc.conjugado((1.5,9)), (1.5,-9))
    
    def test_conversion (self):
        polar = (5, -3)
        normal = (5.830951894845301, 5.742765806909002)
        converted_normal = lc.convertpolarComple(polar)
        converted_polar = lc.convertnormalComple(normal)
        # Compare each component separately
        for a, b in zip(converted_normal, normal):
            self.assertAlmostEqual(a, b, places=10)
        for a, b in zip(converted_polar, polar):
            self.assertAlmostEqual(a, b, places=10)

    def test_fase (self):
        self.assertAlmostEqual(lc.faseComple((3,-1.5)), 5.81953769817)
        self.assertAlmostEqual(lc.faseComple((1,7.5)), 1.438244794498)

if __name__ == '__main__':
    unittest.main()