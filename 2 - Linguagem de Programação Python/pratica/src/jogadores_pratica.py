
class Jogador:
    """Classe que representa o jogador do jogo"""

    def __init__(self, id):
        # O id do jogador sempre será uma string e não pode ser alterado.
        self.__id = str(id)
        self.mao = []
        self.pontos = 0

    @property
    def id(self):
        return self.__id
