import unittest
from sample.Planety import *
from parameterized import *

class PlanetyParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.temp = Planety()

    @parameterized.expand([
        (2134835688,"Merkury",280.88),
        (2134835688,"Wenus",109.96),
        (2134835688,"Mars",35.97),
        (2134835688,"Jowisz",5.7),
        (2134835688,"Saturn",2.3),
        (2134835688,"Uran",0.81),
        (2134835688,"Neptun",0.41)
    ])

    def test_new_wiek_correct(self, sec, planet, res):
        self.assertEqual(self.temp.newWiek(sec, planet), res)

    @parameterized.expand([
        ("Ziemia", 'Ziemia', 'Error in program'),
        (True, False, 'Error in program'),
        (1000, "Marz", 'Error in program')
    ])

    def test_new_wiek_wrong_params(self, sec, planet, res):
        self.assertRaises(Exception, res, self.temp.newWiek, sec, planet)

    def tearDown(self):
        self.temp = None

@parameterized_class(('sec', 'planet', 'expected'), [
        (2134835688,"Saturn",2.3),
        (2134835688,"Uran",0.81),
        (2134835688,"Neptun",0.41)
])

class PlanetyParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.temp = Planety()

    def test_second_parameterized(self):
        self.assertEqual(self.temp.newWiek(self.sec, self.planet), self.expected)

    def tearDown(self):
        self.temp = None

if __name__ == '__main__':
    unittest.main()
