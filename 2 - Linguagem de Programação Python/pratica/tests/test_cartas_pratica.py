import unittest
from src.cartas_pratica import Carta, Naipe, Valor

class TestCartas(unittest.TestCase):

    def test_operacao_relacional_igual(self):
        """Verifica se as condições ao utilizar o operador `==` para comparar 
        as cartas estão atendidas."""
        self.assertTrue(Carta(Naipe.COPAS, Valor.AS) == Carta(Naipe.COPAS, Valor.AS))
        self.assertFalse(Carta(Naipe.OURO, Valor.REI) == Carta(Naipe.COPAS, Valor.REI))
        self.assertFalse(Carta(Naipe.PAUS, Valor.DAMA) == Carta(Naipe.PAUS, Valor.VALETE))
        self.assertFalse(Carta(Naipe.ESPADA, Valor.DEZ) == Carta(Naipe.OURO, Valor.NOVE))
        self.assertFalse(Carta(Naipe.ESPADA, Valor.DEZ) == 'outro tipo')
        self.assertFalse(Carta(Naipe.ESPADA, Valor.DEZ) == None)
        self.assertFalse(Carta(Naipe.ESPADA, Valor.DEZ) is None)
