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


class EnteroARomanoTest(unittest.TestCase):

    def test_transformacionGruposValor(self):
        self.assertEqual(romanos.entero_a_romano(1),'I')
        self.assertEqual(romanos.entero_a_romano(10),'X')
        self.assertEqual(romanos.entero_a_romano(5),'V')
        self.assertEqual(romanos.entero_a_romano(100),'C')
        self.assertEqual(romanos.entero_a_romano(50),'L')
        self.assertEqual(romanos.entero_a_romano(500),'D')
        self.assertEqual(romanos.entero_a_romano(1000),'M')

    def test_transformacionGruposComplejosUnidades(self):
        self.assertEqual(romanos.entero_a_romano(2),'II')
        self.assertEqual(romanos.entero_a_romano(3),'III')
        self.assertEqual(romanos.entero_a_romano(4),'IV')
        self.assertEqual(romanos.entero_a_romano(5),'V')
        self.assertEqual(romanos.entero_a_romano(6),'VI')
        self.assertEqual(romanos.entero_a_romano(7),'VII')
        self.assertEqual(romanos.entero_a_romano(8),'VIII')
        self.assertEqual(romanos.entero_a_romano(9),'IX')
        self.assertEqual(romanos.entero_a_romano(40),'XL')
        self.assertEqual(romanos.entero_a_romano(90),'XC')
        self.assertEqual(romanos.entero_a_romano(3000),'MMM')
        self.assertEqual(romanos.entero_a_romano(400),'CD')
        


    def test_buscaValor(self):
        self.assertEqual(romanos.busca_valor_menor_o_igual(2), ('I',1))
        self.assertEqual(romanos.busca_valor_menor_o_igual(5), ('V',5))
        self.assertEqual(romanos.busca_valor_menor_o_igual(7), ('V',5))

    def test_descomponer(self):
        self.assertEqual(romanos.descomponer(1492), [1000,400,90,2])

    def test_entero_a_romano(self):
        self.assertEqual(romanos.entero_a_romano(1492),'MCDXCII')
        self.assertEqual(romanos.entero_a_romano(3999),'MMMCMXCIX')


if __name__=='__main__':
    unittest.main()
