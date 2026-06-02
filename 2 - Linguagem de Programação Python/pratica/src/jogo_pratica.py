# A classe `Enum` é utilizada para que classes que a herdem se comportem como 
# um enumeration conforme [1].
from enum import Enum
from src.jogadores_pratica import Jogador
from src.croupier_pratica import Croupier
from functools import reduce

class ErroConfiguracao(Exception):
    """Exception definida para tratar erros relacionados a configuração do jogo
    conforme [2]."""
    pass

class ErroInicializacao(Exception):
    """Exception definida para tratar erros relacionados a inicalização do jogo
    conforme [2]."""
    pass

class ErroRodada(Exception):
    """Representa erros que podem acontecer durante a rodada do jogo."""
    pass

class StatusJogo(Enum):
    """Classe `StatusJogo` utilizado para saber a situação do jogo como um
    histórico com base em seus valores, começando em `NAO_CONFIGURADO` (0) indo até
    `FINALIZADO` (3).
    
    A classe herda a `Enum` para que se comporte como um enumeration conforme [1]."""
    NAO_CONFIGURADO = 0
    CONFIGURADO = 1
    INICIADO = 2
    FINALIZADO = 3

class Jogo:
    """Classe que trata funcionalidades relacioandas ao andamento do jogo."""

    ID_JOGADOR_USUARIO = 'Você'
    
    def __init__(self):
        """Inicializa os atributos da classe para que sejam definidos pelo 
        programa ou valores que posteriormente serão configurados pelo jogador
        ou pela lógica do jogo."""

        # Quantidade de jogadores definida pelo jogador.
        self.__numero_jogadores = 0

        # Status do jogo para saber como está o jogo.
        self.__status = StatusJogo.NAO_CONFIGURADO

        # Jogadores que estão jogando o jogo.
        self.__jogadores = {}

        # Quantidade máxima de cartas que podem ser distribuídas a cada rodada.
        self.__quantidade_maxima_cartas = 0

        # Inicializa o objeto que representa o Croupier do jogo.
        self.__croupier = Croupier()

        # Quantidade de cartas a serem entregues na rodada
        self.__quantidade_cartas_rodada = 0
    
    def iniciar(self):
        """Método chamado para iniciar o jogo. O jogo só pode ser iniciado 
        depois de configurado.
        
        Utilizado no método `main` para que o jogo comece."""

        if self.__status == StatusJogo.NAO_CONFIGURADO:
            raise ErroInicializacao('Não é possível iniciar um jogo que não foi configurado.')

        self.__status = StatusJogo.INICIADO
        print("Jogo iniciado!")

    def jogar(self):
        continuar_jogo = True
        while continuar_jogo:
            self.jogar_rodada()
            self.__devolver_cartas()

            while True:
                continuar_jogando = input('Deseja continuar jogando (s/n)? ')

                if continuar_jogando == 's':
                    continuar_jogo = True
                    break
                elif continuar_jogando == 'n':
                    continuar_jogo = False
                    break
                else :
                    print('Resposta inválida, responda com "s" para sim e "n" para não.')
        
        self.sair()

    def sair(self):
        print('Jogo finalizado!') 
        print('Saindo...')
        self.__status = StatusJogo.FINALIZADO

    def jogar_rodada(self):
        """Uma roada é jogada, onde as cartas são entregues para os jogadores e
        em seguida elas são comparadas"""

        # Caso o jogo não esteja iniciado as rodadas não pode ser jogadas pois
        # pode haver configurações pendentes.
        if not self.jogo_iniciado():
            raise ErroRodada("A rodada só pode ser jogada quando o jogo ter sido iniciado.")
        
        # Antes de distribuir as cartas elas são embaralhadas pelo croupier.
        self.__croupier.embaralhar()

        # Define a quantidade de cartas para a rodada, o que definie a quantidade
        # de comparações.
        self.__definir_quantidade_carta_rodada()

        # Laço que se repete até entregar todas as cartas para todos os jogadores.
        for i in range(self.__quantidade_cartas_rodada):
            # Percorre por todos os jogadores utilizando `.values` para entregar 
            # uma carta pra cada
            for jogador in self.__jogadores.values():
                self.__croupier.entregar_carta(jogador)

        self.__contabilizar_rodada()

    def __devolver_cartas(self):
        """Devolve as cartas do jogadores para o baralho do croupier"""
        cartas_utilizadas = []

        for jogador in self.__jogadores.values():
            cartas_utilizadas += jogador.mao[:]
            jogador.mao[:] = []
        
        self.__croupier.devolver_ao_baralho(cartas_utilizadas)

    def __contabilizar_rodada(self): 
        """A rodada é definida pela comparação de várias cartas na ordem em que
        foram recebidas. Vence a rodada quem ganhar mais comparações de cartas."""

        # Há outras maneiras de programar esse método como por exemplo: 
        # - `buscar_cartas_vencidas` poderia ser um atributo de instância.
        # - `mostrar_jogadores` poderia ser um método.
        # 
        # Entre outros, mas para a prática de programação funcional foi 
        # utilizado dessa maneira.

        # Placar da rodada atual para definir quem venceu a rodada
        # um dicionário de chave e valor onde a chave é o id do jogador e o valor
        # é a quantidade de rodadas venciadas.
        cartas_vencidas = {}

        # Funcao definida para que seja utilizada dentro das funções utilizadas
        # no `reduce`. Como o acesso de cartas vencidas está no escopo ela está
        # também disponível dentro da função `buscar_cartas_vencidas`.
        def buscar_cartas_vencidas(id_jogador):
            """busca o placar da rodada atual com base no id do jogador."""

            # retorna 0 caso o jogador ainda não tenha pontuado na rodada, ou 
            # seja seu id não é chave no dicionário.
            return 0 if id_jogador not in cartas_vencidas else cartas_vencidas[id_jogador]
        
        # Laço que percorre de acordo com as `__quantidade_cartas_rodada` 
        # definida pelo usuário.
        for i in range(0, self.__quantidade_cartas_rodada):
            # Mostra qual carta que está sendo comparada, entende-se a primeira
            # carta como a carta de indíce 0, ou Carta 1, e assim por diante. 
            numero_carta = i + 1
            print(f'Carta {numero_carta}')

            # Utilizado o reduce para mostrar os jogadores, assim o parâmetro
            # `texto`, é a variavél retornada em iterações do `reduce`, já
            # o parâmetro `jogador` é o item atual da iteração.
            # Em ambos os retornos é feito uma concatenação da string retornada
            # anteriormente com a string definida agora. 
            def mostrar_jogadores(texto, jogador):
                # A diferença entre os retornos são os espaços antes de mostrar 
                # o placar para que não fique muito desalinhado.
                if jogador.id == Jogo.ID_JOGADOR_USUARIO:
                    return f'{texto} {jogador.id} ({buscar_cartas_vencidas(jogador.id)}) '

                return f'{texto} {jogador.id}   ({buscar_cartas_vencidas(jogador.id)}) '
            
            # Em um exemplo que o jogador J3 já ganhou uma rodada mostra:
            # Você (0)  J1   (0)  J2   (0)  J3   (1)  J4   (0)
            print(reduce(mostrar_jogadores, self.__jogadores.values(), ''))

            # Função definida aqui para poder acessar o indíce atual, este indíce
            # poderia ser passado por parâmetro, novamente é para exercitar outras
            # formas de construir o algoritmo.
            def carta_atual(id_jogador):
                """Recupera a carta do jogador que está sendo comparada atualmente
                na iteração."""
                return self.__jogadores[id_jogador].mao[i]

            # Note que por conta do escopo (bloco) também temos acesso ao indíce
            # que está sendo percorrido no momento (`i`).
            def mostrar_cartas(texto, id_jogador):
                """Mostra a carta do jogador que está sendo comparada no momento."""
                carta = carta_atual(id_jogador)
                # Retorna a carta em texto concatenando com as cartas retornadas
                # nas iterações anteriores.
                return f'{texto}    {carta}    '
                
            # Em exemplo em que há quatro jogadores na rodada, mostra:
            #    2♠        4♣        2♦        J♥        9♥   
            print(reduce(mostrar_cartas, self.__jogadores.keys(), ''))

            # Agora o reduce é utilizado para ao invés de concatenar retornar
            # apenas um resultado com base em comparações de qual carta é maior.
            def definir_jogador_carta_maior(vencedor_atual, id_jogador):
                """Define qual jogador tem a carta maior. Retorna uma tupla para 
                recuperar duas informações ao compara a próxima iteração. 
                A primeira é o id do jogador e a segunda a sua carta para ser 
                comparada em seguida."""

                # carta do jogador que será comparada nessa iteração.
                carta_jogador = carta_atual(id_jogador)

                # se ainda não há vencedor (primeira iteração pois o valor inicial
                # é `None`), então o jogador atual se torna o jogador maior carta.
                if vencedor_atual is None:
                    return (id_jogador, carta_jogador)


                # recupera a carta maior atual a partir da tupla.
                carta_maior_atual = vencedor_atual[1] 

                # se a carta do jogador da iteracao é maior ela se torna a 
                # carta maior para a próxima iteração.
                if carta_jogador > carta_maior_atual:
                    return (id_jogador, carta_jogador)
                # se não, o jogador com a carta maior atual continua sendo o 
                # jogador com a carta maior.
                else :
                    return vencedor_atual

            # Desconstroi a tupla para obter o id do jogador com a carta maior
            # e a carta atual.
            # Note que o valor inicial do `reduce` é `None` para definirmos 
            # internamente em `definir_jogador_carta_maior` o caso do primeiro 
            # jogador.
            id_jogador_vencedor, carta_maior = reduce(definir_jogador_carta_maior, self.__jogadores.keys(), None)

            # No caso do J2 ter vencido com um ás de copas mostra:
            # J2 venceu a carta 1 com A♥
            print(f'{id_jogador_vencedor} venceu a carta {numero_carta} com {carta_maior}')
            
            # Definido o jogador vencedor da primeira comparação é atribuido o
            # resultado ao placar.
            #
            # Inicializa a chave no dicionário com zero caso seja a primeira 
            # pontuação na comparação. 
            if id_jogador_vencedor not in cartas_vencidas:
                cartas_vencidas[id_jogador_vencedor] = 0

            # Incrementa um utilizando o id do jogador vencedor atual.
            cartas_vencidas[id_jogador_vencedor] += 1

        
        def definir_jogador_vencedor_rodada(id_vencedor_atual, id_jogador):
            """De acordo com o número de `cartas_vencidas` define o jogador 
            que ganhou a rodada. """

            # Tratativa para o primeiro item do `reduce` semelhante com 
            # `definir_jogador_carta_maior`.
            if id_vencedor_atual is None:
                return id_jogador
            
            # Reutiliza a função `buscar_cartas_vencidas` do inicio para definir
            # as cartas vencidas do vencedor atual.
            cartas_vencidas_vencedor_atual = buscar_cartas_vencidas(id_vencedor_atual)
            cartas_vencidas_jogador = buscar_cartas_vencidas(id_jogador)

            # Se o jogador da iteração possui mais cartas vencidas que o 
            # vencedor atual ele se torna o novo vencedor atual para a próxima 
            # iteração.
            #
            # Ao final retorna o id do jogador vencedor.
            if cartas_vencidas_jogador > cartas_vencidas_vencedor_atual:
                return id_jogador
            
            return id_vencedor_atual
        
        # Chama a função `definir_jogador_vencedor_rodada` comparando cada 
        # jogador com o próximo.
        id_jogador_vencedor_rodada = reduce(definir_jogador_vencedor_rodada, self.__jogadores, None)
        # Icrementa a quantidade de pontos para o jogador vencedor da rodada.
        self.__jogadores[id_jogador_vencedor_rodada].pontos += 1

        print(f'\n{id_jogador_vencedor_rodada} venceu está rodada!')

        self.__mostrar_placar()

    def __mostrar_placar(self):
        """Mostra o placar após o fim da última rodada"""

        # Utilizando um laço `for` ao invés do `reduce` sendo mais comum.
        placar = 'Placar Atual:\n'
        for jogador in self.__jogadores.values():
            # Diferença de um retorno para o outro está na quantidade de espaços
            if jogador.id == Jogo.ID_JOGADOR_USUARIO:
                placar += f' {jogador.id} [{jogador.pontos}] '
            else :
                placar += f' {jogador.id}   [{jogador.pontos}] '

        # mostra em um caso que o jogador do usuário pontuou:
        # Placar Atual: 
        #  Você [1]  J1   [0]  J2   [0]  J3   [0]
        print(placar)
            

    def __definir_quantidade_carta_rodada(self):
        """Defini a quantidade de cartas que seram entregues na rodada com base 
        no `input` do usuário."""
        while True:
            try:
                # O setter é responsável por verificar se a quantidade informada 
                # é valida.
                self.quantidade_cartas_rodada = int(input('Quantas cartas devem ser entregues nessa rodada? '))
                break
            except ValueError:
                print('Escolha uma quantidade válida para a quantidade de cartas a serem entregues.')
            except ErroRodada as err:
                print(err)


    def configurar(self):
        """Método responsável por configurar o jogo para que ele possa ser jogado
        
        Utilziado no método main para configurar o jogo."""
        self.__definir_quantidade_jogadores()

        self.__popular_jogadores()

        self.__definir_quantidade_maxima_cartas()

        self.__status = StatusJogo.CONFIGURADO


    def __definir_quantidade_jogadores(self):
        """Método utilizado para lidar com o `input` do usuário, verifica se o 
        valor informado é um `int` caso contrário pede para o usuário informar
        um número novamente, desta vez que se ja válido."""
        
        while True:
            """Utilizado laço `while` para que caso algum erro de conversão 
            aconteça o usuário possa informar um novo número. O laço é 
            interrompido utilizando a `break` entendendo que o valor informado 
            para a quantidade de jogaderos é válido."""
            try: 
                # O input do usuário é lido e convertido para `int`
                quantidade_oponentes = int(input('Quantidade de oponentes: '))

                USUARIO = 1
                self.numero_jogadores = quantidade_oponentes + USUARIO
                break
            except ValueError:
                """Caso algum erro de conversão (`ValueError`) seja lançado 
                o erro é tratado para que o usuário possa informar uma quantidade
                de jogadores novamente."""
                print('Escolha um número válido para a quantidade de oponentes.')
            except ErroConfiguracao as err:
                """O `ErroConfiguracao` também e tratado para
                lidar com erros baseados no requisito do jogo definidos no setter 
                de `numero_jogadores`."""
                print(err)

    def __popular_jogadores(self):
        """Define os jogadores do jogo onde o jogador `'Você'` representa o 
        jogador da pessoa que está jogado e demais jogadores representam a máquina."""
        for i in range(self.__numero_jogadores):
            id_jogador = f'J{i}' 

            if i == 0:
                id_jogador = Jogo.ID_JOGADOR_USUARIO

            novo_jogador = Jogador(id=id_jogador)
            self.__jogadores[novo_jogador.id] = novo_jogador

    def __definir_quantidade_maxima_cartas(self):
        """Define a quantidade máxima de cartas com base na quantidade de 
        jogadores configurado para o jogo e com base no número de cartas do
        baralho. 
        
        A quantidade máxima de cartas deve ser um valor inteiro de modo que 
        todos os jogadores possuam a mesma quantidade de cartas, sendo assim:

            quantidade máxima = número de jogadores / quantidade total de cartas no baralho
            Ex:
            quantidade máxima = 3 / 52
            quantidade máxima = 13"""
        
        # Ao converter o resultado da divisão que é `float` para `int` ele acaba
        # removendo os número após a vírgula.
        self.__quantidade_maxima_cartas = int(self.__croupier.quantidade_cartas / self.__numero_jogadores)

    @property
    def numero_jogadores(self):
        """Retorna o número de jogadores"""
        self.__numero_jogadores
    
    @numero_jogadores.setter
    def numero_jogadores(self, numero_jogadores):
        """Define o numero de jogadores
        
        - O jogo deve ter pelo menos dois jogadores e no máximo 52 jogadores 
        que são a quantidade de cartas existentes no baralho. 
        - Não é possível alterar a quantidade de jogadores depois que o jogo foi 
        configurado."""

        # Para lançar exceções em python utiliza-se a palavra reservada `raise`
        # seguido do objeto `Exception`.

        if self.jogo_iniciado():
            raise ErroConfiguracao('Não é possível alterar a quantidade de ' \
            'jogadores após o início do jogo')

        if numero_jogadores < 2:
            raise ErroConfiguracao(
                'O jogo deve possuir pelo menos dois jogadores. ' \
                'Você + quantidade de oponentes.')
        elif numero_jogadores > 52:
            raise ErroConfiguracao(
                'O jogo pode possuir no máximo 52 jogadores. ' \
                'Você + quantidade de oponentes.')

        self.__numero_jogadores = numero_jogadores

    @property
    def quantidade_cartas_rodada(self):
        return self.__quantidade_cartas_rodada
    
    @quantidade_cartas_rodada.setter
    def quantidade_cartas_rodada(self, quantidade_cartas_rodada):
        """São permitidos entre 1 até `self.__quantidade_maxima_cartas` quantidade
        de cartas por rodada."""

        if quantidade_cartas_rodada < 1:
            raise ErroRodada("A quantidade de cartas na rodada deve ser pelo menos 1.")
        elif quantidade_cartas_rodada > self.__quantidade_maxima_cartas:
            raise ErroRodada(f'A quantidade máxima de cartas na rodada é de {self.__quantidade_maxima_cartas}.')
        elif quantidade_cartas_rodada % 2 == 0:
            raise ErroRodada("Não é possível escolher uma " \
            "quantia par de cartas, escolha uma quantia ímpar para que não aconteça empate.")
        
        self.__quantidade_cartas_rodada = quantidade_cartas_rodada

    def jogo__nao_configurado(self):
        """Retorna verdadeiro quando o status do joho é `NAO_CONFIGURADO`"""
        return self.__status == StatusJogo.NAO_CONFIGURADO

    def jogo_configurado(self):
        """Retorna verdadeiro quando o status do jogo é `CONFIGURADO`."""
        return self.__status == StatusJogo.CONFIGURADO
    
    def jogo_iniciado(self):
        """Retorna verdadeiro quando o status do jogo é `INICIADO`."""
        return self.__status == StatusJogo.INICIADO
    
    def jogo_finalizado(self):
        """Retorna verdadeiro quando o status do jogo é `FINALIZADO`."""
        return self.__status == StatusJogo.FINALIZADO 
