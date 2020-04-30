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
        self.assertEqual(romanos.romano_a_entero('K'),'Carácter erróneo')
        self.assertEqual(romanos.romano_a_entero(''), 'Carácter erróneo')

    def test_repetitions(self):
        self.assertEqual(romanos.romano_a_entero('II'),2)
        self.assertEqual(romanos.romano_a_entero('MMM'),3000)
        self.assertEqual(romanos.romano_a_entero('KKK'),'Carácter erróneo')
        self.assertEqual(romanos.romano_a_entero('MK'),'Carácter erróneo')

    def test_decrecientes(self):
        self.assertEqual(romanos.romano_a_entero('XVIII'), 18)
        self.assertEqual(romanos.romano_a_entero('IL'), 'Carácter erróneo')

    def test_3Digitos(self):
        self.assertEqual(romanos.romano_a_entero('IIII'), 'Carácter erróneo')




if __name__=='__main__':
    unittest.main()
