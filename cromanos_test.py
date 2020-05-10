import unittest
import cromanos

class RomanNumberTest(unittest.TestCase):

    def test_crea_romano(self):
        nr = cromanos.RomanNumber(25)
        self.assertEqual(nr.value, 25)
        self.assertEqual(nr.romanValue, 'XXV')

        snr = cromanos.RomanNumber('XXIV')
        self.assertEqual(snr.value, 24)
        self.assertEqual(snr.romanValue, 'XXIV')

        tnr = cromanos.RomanNumber('XXXX')
        self.assertEqual(tnr.value, 'Error de formato')
        self.assertEqual(tnr.romanValue, 'Error de formato')

        cnr = cromanos.RomanNumber(0)
        self.assertEqual(cnr.value, 'Overflow')
        self.assertEqual(cnr.romanValue, 'Overflow')

        qnr = cromanos.RomanNumber(4000)
        self.assertEqual(qnr.value, "Overflow")
        self.assertEqual(qnr.romanValue, "Overflow")

    def test_representation(self):
        nr = cromanos.RomanNumber(25)
        self.assertEqual(str(nr), 'XXV')
        #self.assertEqual(nr, 'XXV')

    def test_equal_romans(self):
        nr1 = cromanos.RomanNumber(25)
        nr2 = cromanos.RomanNumber('XXV')
        self.assertEqual(nr1, nr2)

    def test_add_roman(self):
        nr1 = cromanos.RomanNumber(1)
        nr2 = cromanos.RomanNumber('XXIV')
        nr3 = nr1+nr2 
        self.assertEqual(nr1+nr2, cromanos.RomanNumber(25))
        self.assertEqual(nr3.value, 25)
        self.assertTrue(isinstance(nr3, cromanos.RomanNumber))

    def test_add_integer(self):
        nr1 = cromanos.RomanNumber('XXIII')
        nr3 = nr1 + 1
        self.assertEqual(nr3.value, 24)
        self.assertTrue(isinstance(nr3, cromanos.RomanNumber))

        nr2 = 1 + nr1
        self.assertEqual(nr2.value, 24)
        self.assertTrue(isinstance(nr2, cromanos.RomanNumber))

    def test_resta_roman(self):
        nr1= cromanos.RomanNumber(25)
        nr2= cromanos.RomanNumber('XV')
        nr3= nr1- nr2
        self.assertEqual(nr1- nr2, cromanos.RomanNumber(10))
        self.assertEqual(nr3.value, 10)
        self.assertTrue(isinstance(nr3,cromanos.RomanNumber ))

    def test_resta_integer(self):
        nr1= cromanos.RomanNumber('XXV')
        nr3= nr1- 10
        self.assertEqual(nr3.value, 15)
        self.assertTrue(isinstance(nr3, cromanos.RomanNumber))

        nr2= 35- nr1
        self.assertEqual(nr2.value, 'Overflow')  #no hay propiedad conmutativa en las restas (pasa por el __sub__)
        self.assertTrue(isinstance(nr2, cromanos.RomanNumber))

    def test_multip(self):
        nr1= cromanos.RomanNumber(3)
        nr2= cromanos.RomanNumber('XXV')
        nr3= nr1*nr2
        self.assertEqual(nr1*nr2, cromanos.RomanNumber(75))
        self.assertEqual(nr3.value, 75)
        self.assertTrue(isinstance(nr3, cromanos.RomanNumber))

    def test_mult_integer(self):
        nr1= cromanos.RomanNumber('XXV')
        nr2= nr1*3
        self.assertEqual(nr1*3, cromanos.RomanNumber(75))
        self.assertEqual(nr2.value, 75)
        self.assertTrue(isinstance(nr2, cromanos.RomanNumber))

        nr3= 4*nr1
        self.assertEqual(nr1*4, cromanos.RomanNumber(100))
        self.assertEqual(nr3.value, 100)
        self.assertTrue(isinstance(nr3, cromanos.RomanNumber))

    def test_divis(self):
        nr1= cromanos.RomanNumber(3)
        nr2= cromanos.RomanNumber('XXVII')
        nr3= nr2/ nr1
        self.assertEqual(nr2/nr1, cromanos.RomanNumber(9))
        self.assertEqual(nr3.value, 9)
        self.assertTrue(isinstance(nr3, cromanos.RomanNumber))

    def test_divis_integer(self):
        nr1= cromanos.RomanNumber('XXVII')
        nr2= nr1/3
        self.assertEqual(nr1/3, cromanos.RomanNumber(9))
        self.assertEqual(nr2.value, 9)
        self.assertTrue(isinstance(nr2, cromanos.RomanNumber))

        





    

        




if __name__ == '__main__':
    unittest.main() 