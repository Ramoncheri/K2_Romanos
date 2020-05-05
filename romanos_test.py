import unittest
import romanos

class RomanNumberTest(unittest.TestCase):

    def test_symbols_romans(self):
        self.assertEqual(romanos.romano_a_entero('I'),1)
        self.assertEqual(romanos.romano_a_entero('V'),5)
        self.assertEqual(romanos.romano_a_entero('X'),10)
        self.assertEqual(romanos.romano_a_entero('L'),50)
        self.assertEqual(romanos.romano_a_entero('C'),100)
        self.assertEqual(romanos.romano_a_entero('D'),500)
        self.assertEqual(romanos.romano_a_entero('M'),1000)
        self.assertEqual(romanos.romano_a_entero('K'),'Error de formato')
        self.assertEqual(romanos.romano_a_entero(''), 'Error de formato')

    def test_repetitions(self):
        self.assertEqual(romanos.romano_a_entero('II'),2)
        self.assertEqual(romanos.romano_a_entero('MMM'),3000)
        self.assertEqual(romanos.romano_a_entero('KKK'),'Error de formato')
        self.assertEqual(romanos.romano_a_entero('MK'),'Error de formato')

    def test_decrecientes(self):
        self.assertEqual(romanos.romano_a_entero('XVIII'), 18)
        self.assertEqual(romanos.romano_a_entero('IX'),9)
        self.assertEqual(romanos.romano_a_entero('IL'), 'Error de formato')
        self.assertEqual(romanos.romano_a_entero('XI'),11)
        self.assertEqual(romanos.romano_a_entero('CI'),101)
        self.assertEqual(romanos.romano_a_entero('XXI'),21)
        self.assertEqual(romanos.romano_a_entero('XD'), 'Error de formato')
        

    def test_restaMultiplos5(self): 
        self.assertEqual(romanos.romano_a_entero('VX'), 'Error de formato')
        self.assertEqual(romanos.romano_a_entero('LC'), 'Error de formato')
        self.assertEqual(romanos.romano_a_entero('XCV'), 95)
        

    def test_3Digitos(self):
        self.assertEqual(romanos.romano_a_entero('IIII'), 'Error de formato')

    def test_resta1soloSimbolo(self):
        self.assertEqual(romanos.romano_a_entero('XXL'), 'Error de formato')
        self.assertEqual(romanos.romano_a_entero('IXL'), 'Error de formato')



if __name__=='__main__':
    unittest.main()
