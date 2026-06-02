# A função `randint` retorna um número aleatório dentro do intervalo informado [12].
from random import randint
from src.cartas_pratica import Carta, Naipe, Valor

class Croupier:
    """Classe responsável por modelar a função do croupier em jogos de carta.
    
    A função dessa classe é gerenciar o baralho do jogo. 
    
    Por padrão o baralho utilizado possui 52 cartas semelhante ao baralho comum."""

    def __init__(self):
        # self.__baralho = [i for i in range(52)]
        # Podemos percorrer uma enum de forma semelhante a uma lista [1].
        # Podemos percorrer duas listas utilizando list comprehension [10].
        # Desta maneira inicializamos o baralho com todas as cartas sem repetir.
        self.__baralho = [Carta(naipe, valor) for naipe in Naipe for valor in Valor]

    @property
    def quantidade_cartas(self):
        """Retorna a quantidade de cartas do baralho. Por padrão o baralho 
        possui 52 cartas."""
        return len(self.__baralho)
    
    def embaralhar(self):
        """Embaralha as cartas de forma aleatória pegando cartas do meio do 
        baralho e colocando-as no topo de maneira contrária dividido em novos 
        intervalos a partir do primeiro intervalo"""

        # Quantidade de vezes que o baralho será embaralhado é definido por um
        # número aleatório entre 50 a 100.
        vezes_embaralhar = randint(50, 100)

        # Faz o processo de embaralhar diversas vezes para que o baralho 
        # se misture.
        while vezes_embaralhar > 0:
            # Defini o intervalo aleatorio onde:
            # o inicio é entre a primeira até a carta do meio do baralho. 
            inicio = randint(0, self.quantidade_cartas / 2)
            # o fim é da próxima carta a partir do inicio (`inicio` + 1) até
            # o total de cartas do baralho.
            fim = randint(inicio + 1, self.quantidade_cartas)

            # Dessa maneira temos um intervalo definido entre a primeira e a 
            # metade do baralho. 
            # Pega as cartas do meio do baralho definida utilizando o `slice`.
            intervalo_inicial = self.__baralho[inicio: fim]

            # Removemos as cartas pegas para o intervalo assim as cartas não
            # estão mais no meio do baralho.
            # A palavra reservada `del` remove os itens da lista [10].
            del self.__baralho[inicio: fim]
            
            # Agora com as cartas do intervalo vamos colocar fatias delas no
            # topo do baralho, de forma semelhante ao embaralhar cartas.
            fatias_intervalo = []
            # Fazemos isso até dividir todo o baralho em fatias, por isso o uso
            # do `while`.
            while len(intervalo_inicial) > 0:
                # A quantidade de cada fatia também é definida aleatoriamente.
                tamanho_fatia = randint(0, len(intervalo_inicial))

                # Se o tamanho da fatia é maior que o intervalo que foi pego
                # inicialmente utiliza todo o restante do intervalo. 
                if tamanho_fatia > (len(intervalo_inicial)):
                    # pega o restante do intervalo inicial e adiciona no topo do 
                    # baralho concatenando as listas [13].
                    self.__baralho = intervalo_inicial + self.__baralho
                    # limpa o que sobrou do intervalo inicial sendo essa a 
                    # condição de parada do laço `while` uma vez que agora o 
                    # intervalo inicial está vazio, ou seja todas as cartas
                    # foram para o topo do baralho.
                    del intervalo_inicial[:]
                else :
                    # pega a nova fatia e adiciona no topo do baralho
                    # concatenando as listas [13].
                    self.__baralho = intervalo_inicial[:tamanho_fatia] + self.__baralho
                    del intervalo_inicial[:tamanho_fatia]
                
            # decrementa a váriavel indicando que falta menos vezes para embaralhar
            vezes_embaralhar -= 1

    def entregar_carta(self, jogador):
        """Remove uma carta do topo do baralho e entrega para a mão do jogador."""
        jogador.mao.append(self.__baralho.pop(0))

    def devolver_ao_baralho(self, cartas):
        """Devolve as cartas para o fundo do baralho."""
        self.__baralho.extend(cartas)
