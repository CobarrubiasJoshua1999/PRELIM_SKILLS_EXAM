from cobarrubias_temp import Temperature
import unittest

print(Temperature) 

class Kelvin_Test(unittest.TestCase):
    def test_celsius(self):
        self.assertEqual(Temperature(celsius=10).kelvin,float,(283.15))

    def test_fahrenheit(self):
        self.assertEqual(Temperature(fahrenheit=10).kelvin,float,(260.928))

    def test_kelvin(self): 
        self.assertEqual(Temperature(kelvin=17).kelvin,17)

    def test_noArg(self): 
        self.assertEqual(Temperature(kelvin=-1).kelvin,-1)

if __name__ == '__main__':
    unittest.main()