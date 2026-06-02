from enum import Enum

class Naipe(Enum):
    """Representa o Naipe dos baralhos, onde cada Naipe tem um valor maior que 
    o outro, para critério de desempate o naipe com valor maior vence.
    
    O Maior naipe é o `PAUS` e o menor o `OURO`."""

    # `\u` é utilizado para lidar com unicodes em python [7].
    # Emojis em unicode para representãção do Naipe no terminal de acordo
    # com o unicode do site disponível em [8].
    PAUS = ('\u2663', 4)
    COPAS = ('\u2665', 3)
    ESPADA = ('\u2660', 2)
    OURO = ('\u2666', 1)

    @property
    def icone(self):
        """Retorna o primeiro elemento da tupla que representa o `icone` do naipe."""
        return self.value[0]
    
    @property
    def peso(self):
        """Retorna o segundo elemento da tupla que representa o `peso` do naipe."""
        return self.value[1]

class Valor(Enum):
    """Valor representa o valor de cada carta onde a carta mais alta é a que 
    possui o valor maior.
    
    Dessa forma a carta mais alta é o `AS` e a mais baixa o `DOIS`.s"""
    
    AS = ('A', 13)
    REI = ('K', 12)
    DAMA = ('Q', 11)
    VALETE = ('J', 10)
    DEZ = ('10', 9)
    NOVE = ('9', 8)
    OITO = ('8', 7)
    SETE = ('7', 6)
    SEIS = ('6', 5)
    CINCO = ('5', 4)
    QUATRO = ('4', 3)
    TRES = ('3', 2)
    DOIS = ('2', 1)

    @property
    def sigla(self):
        """Retorna o primeiro elemento da tupla que representa o `sigla` da carta."""
        return self.value[0]
    
    @property
    def peso(self):
        """Retorna o segundo elemento da tupla que representa o `peso` da carta."""
        return self.value[1]

class Carta:
    """Classe que representa as cartas do baralho. Uma carta possui um `Naipe`
    e um `valor`. """

    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    # Sobrescreve a operação relacional de igualdade (operador `==`) de um objeto. 
    def __eq__(self, outra_carta):
        # Primeiro compara os tipos, caso não seja uma `Carta` já é diferente.
        if type(self) != type(outra_carta):
            return False
        
        # Retorna verdadeiro se o naipe e valor das cartas forem iguais
        return self.naipe == outra_carta.naipe and self.valor == outra_carta.valor 
    
    # Define a operação relacional quando o operador `>` é utilizado [9]. 
    def __gt__(self, outra_carta):
        """Retorna verdadeiro se o peso do valor da carta (`self`) for maior que 
        o peso do valor da `outra_carta`, se não retorna falso..
        
        Caso ambas as cartas possuam o mesmo valor o naipe é comparado, retorna
        verdadeiro se o peso do naipe da carta é maior que o peso do naipe da 
        `outra_carta`, se não retorna falso."""
        
        if self.valor.peso == outra_carta.valor.peso:
            return self.naipe.peso > outra_carta.naipe.peso
        else:
            return self.valor.peso > outra_carta.valor.peso

    def mostrar(self):
        """Mostra o valor e naipe da carta"""
        return f'{self.valor.sigla}{self.naipe.icone}'

    def __str__(self):
        """Sobrescreve o método utilizado para converter a classe em um `str` 
        conforme [9].
        
        Utilizado para quando mostrar a carta no terminal."""
        return self.mostrar()
    
    def __repr__(self):
        """Sobrescreve o método que define a representação oficial do objeto em 
        String [9].
        
        Utilizado para quando mostrar a carta no terminal."""
        return self.mostrar()
        