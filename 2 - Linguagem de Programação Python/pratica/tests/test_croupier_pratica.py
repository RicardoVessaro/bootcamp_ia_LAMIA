import unittest
from src.croupier_pratica import Croupier
from src.cartas_pratica import Carta

class TestCrupier(unittest.TestCase):
    
    def test_baralho_croupier(self):
        """Verifica se o baralho do crupier foi incializado de forma correta.
        Sendo o baralho composto por `Cartas` e não são repetidas."""

        croupier = Croupier()
        baralho = croupier._Croupier__baralho

        self.assertEqual(52, len(baralho))

        self.assert_baralho_completo(baralho)

        print(croupier._Croupier__baralho)

    def test_embaralhar(self):
        """Verifica se o baralho foi embaralhado e está completo."""
        
        croupier = Croupier()

        # for i in range(3):
        # `.copy()` retorna uma cópia da lista para que não tenha a mesma 
        # referência em memória. [10]
        baralho_inicial = croupier._Croupier__baralho.copy()

        croupier.embaralhar()

        baralho_embaralhado = croupier._Croupier__baralho.copy()

        # Mostra o baralho para ver ele embaralhado ao executar os testes.
        print(baralho_embaralhado)
        self.assertFalse(self.is_baralho_mesma_ordem(baralho_inicial, baralho_embaralhado))
        self.assert_baralho_completo(baralho_embaralhado)


    def assert_baralho_completo(self, baralho):
        """Verifica se o baralho possui todas as cartas e não está repetido."""
        baralho_conferido = []
        # Percorre as cartas no baralho
        for carta in baralho:
            # Verifica se o baralho é composto de cartas. A função built-in 
            # `isinstance` retorna verdadeiro se a variável é uma instância
            # da classe informada no segundo parâmetro [11].
            if not isinstance(carta, Carta):
                # `fail` faz com o queste falhe caso entre no bloco do `if` [3].
                self.fail(f'Deve utilizar um baralho de cartas e não {type(carta)}.')

            # Percorre as cartas já verificadas para confirmar que não há cartas
            # repetidas no baralho.
            for carta_ja_verificada in baralho_conferido:
                # Se a carta que está sendo percorrida é igual a uma carta
                # já verificada significa que há cartas repetidas no baralho.
                if carta == carta_ja_verificada: 
                    self.fail(f'A carta {carta} está repetida.')
                
            # Caso a carta não esteja repetida ela vai para o baralho de cartas
            # já verificadas.
            baralho_conferido.append(carta)

    def test_is_baralho_mesma_ordem(self):
        """Verifica se a ordem dos baralhos está verifcada de maneira correta"""

        # Retorna True pois os baralhos não tiveream a ordem alterada
        self.assertTrue(
            self.is_baralho_mesma_ordem(
                Croupier()._Croupier__baralho, Croupier()._Croupier__baralho)
        )

        # Retorna false pois comparamos um baralho que foi revertido uilizando o 
        # `revert()` que inverte os elementos da lista [10].
        baralho_invertido = Croupier()._Croupier__baralho
        baralho_invertido.reverse()
        self.assertFalse(
            self.is_baralho_mesma_ordem(Croupier()._Croupier__baralho, baralho_invertido)
        )

    def is_baralho_mesma_ordem(self, baralho_left, baralho_right):
        """Retorna verdadeiro se os dois baralhos informados estão com as cartas
        na mesma ordem. Retorna falso caso não estejam. O teste falha caso 
        informe baralhos de tamanhos diferentes."""
        if len(baralho_left) != len(baralho_right):
            self.fail('Os baralhos devem possuir o mesmo tamanho para serem comparados.')

        for i in range(len(baralho_left)):
            if baralho_left[i] != baralho_right[i]:
                return False
            
        return True
