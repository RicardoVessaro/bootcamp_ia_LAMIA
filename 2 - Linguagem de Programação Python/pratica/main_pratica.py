
from src.jogo_pratica import Jogo
from src.cartas_pratica import Naipe

# Definição do arquivo main quando for o ponto de execução do interpretador.
if __name__ == '__main__':
    jogo = Jogo()
    jogo.configurar()
    jogo.iniciar()
    jogo.jogar()
