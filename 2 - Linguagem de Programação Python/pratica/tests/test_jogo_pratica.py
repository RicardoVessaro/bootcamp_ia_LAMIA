# Módulo utilizado para testes unitários em python [3].
import unittest
# `unittest.mock`: Módulo utilizado para simular retornos de métodos de outras
# classes [6].
# `patch`: Utilizado para simula retornos de chamadas de funções ou métodos [6].
# `call`: Utilziado para montar objeto que representa uma chamada de um método [6].
from unittest.mock import patch, call
from src.jogo_pratica import Jogo, ErroConfiguracao, ErroInicializacao, ErroRodada
from src.cartas_pratica import Carta, Naipe, Valor

# Toda a classe de teste herda `unittest.TestCase` [3].
class TestJogo(unittest.TestCase):

    # Método utilizado para preparar o cenário para o teste antes do teste ser 
    # executado. Este método é chamado de cada teste [3].
    def setUp(self):
        self.jogo = Jogo()

    def test_jogo_comeca_com_status_NAO_CONFIGURADO(self):
        """Verifica o requisito de inicar o jogo com o status NAO_CONFIGURADO"""
        # Realiza a asserção do teste [3].
        self.assertTrue(self.jogo.jogo__nao_configurado())

    def test_jogo_deve_possuir_pelo_menos_dois_jogadores(self):
        """Verifica o requisito do jogo possuir pelo menos dois jogadores"""

        # `with` é a palavara reservada utilizada para empacotar o trecho de 
        # código que será utilizado pelo contexto e atribuir o retorno para o 
        # `target` caso definido utilizado a palavra reservada `as`, neste caso
        # o target é a variável `err` [4].
        # Contexto executa o código definido dentro do bloco `with` e no retorno
        # para atribuir o `target` informa se alguma exceção foi suprimida. [5]
        # `self.assertRaises` verifica se o bloco de código lança a exceção 
        # definida, no caso `ErroConfiguracao` [3].
        with self.assertRaises(ErroConfiguracao) as err:
            # Trecho do código que deve gerar o erro para ser tratado pelo 
            # contexto do `assertRaises` [3].
            self.jogo.numero_jogadores = 1

        # Compara se a mensagem informada na exceção lançada é a mensagem 
        # esperada de acordo com o cenário de teste [3].
        # Para acessar a exceção utiliza `err.exception`  e convertendo-a em 
        # `str` é possível ter a mensagem de erro.
        self.assertEqual(str(err.exception), 
                'O jogo deve possuir pelo menos dois jogadores. ' \
                'Você + quantidade de oponentes.')
    
        # Código que não é para lançar exceção pois cumpre com os requisitos
        self.jogo.numero_jogadores = 2

    def test_jogo_pode_possuir_no_maximo_53_jogadores(self):
        """Verifica o requisito do jogo permitir no máximo 52 jogadores."""

        with self.assertRaises(ErroConfiguracao) as err:
            self.jogo.numero_jogadores = 53

        self.assertEqual(str(err.exception), 
                'O jogo pode possuir no máximo 52 jogadores. ' \
                'Você + quantidade de oponentes.')
        
        # Verifica se o número 52 é permitido uma vez que caso lance algum erro
        # o teste falha.
        self.jogo.numero_jogadores = 52

    def test_status_jogo_esta_como_INICIADO_apos_configurado_quando_iniciar(self):
        """Verifica se depois de iniciado o jogo o status muda para INCIADO quando iniciar"""

        # O `patch` é utilizado para imitar o retorno de uma função definida. 
        # Neste caso o `patch` está sendo utilizado como context manager para
        # simular a entrada de um valor digitado no terminal quando a função 
        # `input` do pacote `builtins` é utilizada. O Valor definido para ser 
        # utilizado como retorno da função é definido no parâmetro `return_value` 
        # [6].
        with patch('builtins.input', side_effect=["1", "1"]):
            # `.iniciar` precisa da entrada do usuário para definir a quantidade
            # de oponentes por isso dele é simulado no teste.
            self.jogo.configurar()
            self.jogo.iniciar()

            # Em seguida verificamos se o status do jogo mudou para INICIADO.
            self.assertTrue(self.jogo.jogo_iniciado())
    
    def test_status_jogo_esta_como_CONFIGURADO_apos_configurar(self):
        """Verifica se quando configurado status do jogo muda para CONFIGURADO"""

        with patch('builtins.input', return_value="1"):
            self.jogo.configurar()
        
        self.assertTrue(self.jogo.jogo_configurado())
        
    # mocks (simulação do método) pode ser utilizado na forma de `decorator`
    # e assim referenciado a partir do parâmetro no método, no caso o parâmetro
    # `mock_print` [6]. 
    @patch('builtins.print')
    def test_deve_mostrar_mensagem_ao_informar_um_valor_que_nao_seja_int_para_quantidade_oponentes(
        self, mock_print):
        """Verifica se a entrada do valor ao pedir a quantidade de oponentes pelo
        terminal está sendo tratada para permitir apenas números inteiros (`int`)
        com a seguinte mensagem:
        'Escolha um número válido para a quantidade de oponentes.'"""

        # O parâmetro `side_effect` faz com que a cada interação com o método
        # imitado (mock) retorna um novo valor na lista, assim verficamos varias
        # entradas para o input e por último informamos uma entrada válida [6].
        with patch('builtins.input', side_effect=['abcd', '1.1', '', '1']):
            # Ao chamar a função `input` ela retornará os valores definidos em 
            # `side_effect`
            self.jogo.configurar()
            chamadas = [call('Escolha um número válido para a quantidade de oponentes.')]
            mock_print.assert_has_calls(chamadas, any_order=True)

    def test_nao_permitir_iniciar_jogo_que_nao_foi_configurado(self):
        """Verifica o requisito de somente inciar o jogo após configurado"""

        with self.assertRaises(ErroInicializacao) as err:
            self.jogo.iniciar()

        self.assertEqual(str(err.exception), 'Não é possível iniciar um jogo que não foi configurado.')

    def test_jogadores_configurados_acordo_numero_jogadores(self):
        """Verifica se os jogadores estão configurados de acordo com a 
        quantidade de oponentes mais o usuário definido como `Você`."""

        with patch('builtins.input', return_value="2"):
            self.jogo.configurar()
        
        # Quebra o encapsulamento conforme demonstrado na aula. 
        jogadores = self.jogo._Jogo__jogadores
        # Verifica se possui 3 jogadores configurados.
        self.assertEqual(3, len(jogadores))
        # Verifica se os ids estão definidos conforme o esperado.
        id_jogadores = ['Você', 'J1', 'J2']
        for jogador in jogadores.values():
            # informando uma mensagem de erro através do parâmetro `msg` caso a 
            # verificação falhe. Útil para debug.
            self.assertTrue(jogador.id in id_jogadores,
                msg=f'Jogador `{jogador.id}` não está configuardo de acordo com: {id_jogadores}.')


    def test_definir_quantidade_maxima_possivel_de_cartas_para_rodada(self):
        """Verifica se a quantidade máxima de cartas está correta para o jogo.
        
        A quantidade máxima de cartas é dada por:
            quantidade máxima = número de jogadores / quantidade total de cartas 
            quantidade máxima = 4 / 52
            quantidade máxima = 13

        Exemplo se no jogo há 4 jogadores a quantidade máxima de cartas para cada
        jogador é de 13. A conta deve considerar um valor inteiro para a 
        quantidade máxima de cartas para que não falte carta e nenhum jogador
        fique com uma quantidade maior de cartas."""

        # Função utilizada para verificar conforme os parâmetros.
        def assert_quantidade_cartas(numero_oponentes, quantidade_esperada):
            with patch('builtins.input', return_value=numero_oponentes):
                self.jogo.configurar()
                self.assertEqual(
                    quantidade_esperada, self.jogo._Jogo__quantidade_maxima_cartas, 
                    msg=f'Quantidade esperada: {quantidade_esperada}, Quantidade calculada: {self.jogo._Jogo__quantidade_maxima_cartas}.')

        # Os parâmetros representam os cenários de teste, assim ao utilizar a
        # função `assert_quantidade_cartas` podemos verificar diveros cenários 
        # de teste.
        assert_quantidade_cartas(numero_oponentes="3", quantidade_esperada=13)
        assert_quantidade_cartas(numero_oponentes="2", quantidade_esperada=17)
        assert_quantidade_cartas(numero_oponentes="1", quantidade_esperada=26)
        assert_quantidade_cartas(numero_oponentes="51", quantidade_esperada=1)

    @patch('builtins.print')
    def test_quantidade_cartas_permitidas_para_rodada_eh_int(self, mock_print):
        """Verifica se a quantidade de cartas informadas é do tipo `int`"""

        with patch('builtins.input', side_effect = ['1', 'abcd', '9.1', '1']):

            self.jogo.configurar()
            self.jogo.iniciar()
            self.jogo.jogar_rodada()
            chamadas = [call('Escolha uma quantidade válida para a quantidade de cartas a serem entregues.')]
            mock_print.assert_has_calls(chamadas, any_order=True)
        
    def test_quantidade_cartas_permitidas_para_rodada(self):
        """Verifica se está validando a quantidade de cartas permitidas na rodada
        com base na quantidade máxima de cartas permitidas. E se a quantidade de cartas 
        é positiva."""

        quantidade_oponentes = '3'
        with patch('builtins.input', return_value = quantidade_oponentes):
            self.jogo.configurar()

        with self.assertRaises(ErroRodada) as err:
            self.jogo.quantidade_cartas_rodada = 0
        self.assertEqual(str(err.exception), "A quantidade de cartas na rodada deve ser pelo menos 1.")

        with self.assertRaises(ErroRodada) as err:
            self.jogo.quantidade_cartas_rodada = 14
        self.assertEqual(str(err.exception), "A quantidade máxima de cartas na rodada é de 13.")

    def test_deve_permitir_jogar_a_rodada_apenas_quando_jogo_iniciado(self):
        """Verifica se a rodada pode ser jogada apenas depois do jogo iniciado."""

        with self.assertRaises(ErroRodada) as err:
            self.jogo.jogar_rodada()
        self.assertEqual(str(err.exception), "A rodada só pode ser jogada quando o jogo ter sido iniciado.")

    def test_deve_entregar_quantidade_correta_cartas_para_cada_jogador(self):
        """Verifica se todos os jogadores possuem as mesmas quantidade de cartas."""

        self.__inicar_jogo()
        quantidade_cartas = '3'
        with patch('builtins.input', return_value = quantidade_cartas):
            self.jogo.jogar_rodada()

        jogadores = self.jogo._Jogo__jogadores

        for id, jogador in jogadores.items():
            self.assertEqual(int(quantidade_cartas), len(jogador.mao))
            for carta in jogador.mao:
                self.assertTrue(isinstance(carta, Carta))

    def test_deve_atribuir_corretamente_os_pontos_para_cada_jogador(self):

        self.__inicar_jogo()
        
        # Definindo a quantidade de cartas utilizadas na rodada.
        self.jogo.quantidade_cartas_rodada = 3

        # Simulamos as cartas dos jogadores para poder testar a pontuação.
        self.__jogador('Você').mao = [Carta(Naipe.PAUS, Valor.AS), Carta(Naipe.OURO, Valor.DOIS), Carta(Naipe.PAUS, Valor.REI)]
        self.__jogador('J1').mao = [Carta(Naipe.PAUS, Valor.REI), Carta(Naipe.PAUS, Valor.TRES), Carta(Naipe.OURO, Valor.REI)]
        self.__jogador('J2').mao = [Carta(Naipe.PAUS, Valor.VALETE), Carta(Naipe.COPAS, Valor.CINCO), Carta(Naipe.COPAS, Valor.REI)]
        self.__jogador('J3').mao = [Carta(Naipe.PAUS, Valor.DAMA), Carta(Naipe.ESPADA, Valor.QUATRO), Carta(Naipe.ESPADA, Valor.REI)]
        
        # Contabiliza a rodada para ver qual jogador ganhou.
        self.jogo._Jogo__contabilizar_rodada()

        # Contabilizada a rodada deve atribuir um ponto para o jogador vencedor.
        self.assertEqual(1, self.__jogador('Você').pontos)
        self.assertEqual(0, self.__jogador('J1').pontos)
        self.assertEqual(0, self.__jogador('J2').pontos)
        self.assertEqual(0, self.__jogador('J3').pontos)

        # Definindo uma quantidade de cartas para a nova rodada.
        self.jogo.quantidade_cartas_rodada = 1

        # Jogada mais uma rodada para verificar se os pontos são somados.
        self.__jogador('Você').mao = [Carta(Naipe.OURO, Valor.CINCO)]
        self.__jogador('J1').mao = [Carta(Naipe.COPAS, Valor.DOIS)]
        self.__jogador('J2').mao = [Carta(Naipe.PAUS, Valor.QUATRO)]
        self.__jogador('J3').mao = [Carta(Naipe.ESPADA, Valor.TRES)]

        self.jogo._Jogo__contabilizar_rodada()
        
        # Verifica se o ponto foi somado corretamente.
        self.assertEqual(2, self.__jogador('Você').pontos)
        self.assertEqual(0, self.__jogador('J1').pontos)
        self.assertEqual(0, self.__jogador('J2').pontos)
        self.assertEqual(0, self.__jogador('J3').pontos)

        # Terceira rodada onde outro jogador ganha para contabilizar pontos 
        # para outro jogador vencedor.
        self.jogo.quantidade_cartas_rodada = 1

        self.__jogador('Você').mao = [Carta(Naipe.PAUS, Valor.QUATRO)]
        self.__jogador('J1').mao = [Carta(Naipe.COPAS, Valor.DOIS)]
        self.__jogador('J2').mao = [Carta(Naipe.OURO, Valor.CINCO)]
        self.__jogador('J3').mao = [Carta(Naipe.ESPADA, Valor.TRES)]

        self.jogo._Jogo__contabilizar_rodada()
        
        # Verifica se os jogadores mantiveram seus pontos e o vencedor ganhou 
        # um ponto.
        self.assertEqual(2, self.__jogador('Você').pontos)
        self.assertEqual(0, self.__jogador('J1').pontos)
        self.assertEqual(1, self.__jogador('J2').pontos)
        self.assertEqual(0, self.__jogador('J3').pontos)

        # Quarta rodada onde há um empate, neste caso ambos os jogadores pontuam
        self.jogo.quantidade_cartas_rodada = 2

        self.__jogador('Você').mao = [Carta(Naipe.PAUS, Valor.AS), Carta(Naipe.COPAS, Valor.REI)]
        self.__jogador('J1').mao = [Carta(Naipe.COPAS, Valor.OITO), Carta(Naipe.OURO, Valor.AS)]
        self.__jogador('J2').mao = [Carta(Naipe.OURO, Valor.SETE), Carta(Naipe.COPAS, Valor.TRES)]
        self.__jogador('J3').mao = [Carta(Naipe.PAUS, Valor.TRES), Carta(Naipe.COPAS, Valor.AS)]

        self.jogo._Jogo__contabilizar_rodada()
        
        # Verifica se os jogadores mantiveram seus pontos e os vencedores 
        # ganharam um ponto cada.
        self.assertEqual(3, self.__jogador('Você').pontos)
        self.assertEqual(0, self.__jogador('J1').pontos)
        self.assertEqual(1, self.__jogador('J2').pontos)
        self.assertEqual(1, self.__jogador('J3').pontos)


    @patch('builtins.print')
    def test_permitir_jogador_sair_do_jogo_apos_o_fim_da_rodada(self, mock_print):
        """Verifica se o usuário pode sair do jogo sem ter que terminar a 
        execução do programa."""

        # inicalizar o jogo
        self.__inicar_jogo()


        quantidade_cartas = '1' # resposta para a quantiade de cartas.
        continuar_jogando = 's' # resposta para continuar jogando e jogar mais
                                # uma rodada.
        resposta_invalida = 'a' # resposta inválida para que exija uma resposta
                                # válida
        sair_do_jogo = 'n'  # resposta para sair do jogo
        # define as respostas do inputs com `side_effect` [6].
        with patch('builtins.input', side_effect = [
            quantidade_cartas, continuar_jogando, quantidade_cartas, 
            resposta_invalida, sair_do_jogo]) as mock_input:

            self.jogo.jogar()

        # Confere se a pergunta foi feita de forma esperada.
        chamadas_input = [
            call('Deseja continuar jogando (s/n)? '),
        ]
        mock_input.assert_has_calls(chamadas_input, any_order=True)

        # Confere se as respostas foram mostradas para o usuário.
        chamadas_print = [
            call('Resposta inválida, responda com "s" para sim e "n" para não.'),
            call('Jogo finalizado!'),
        ]
        mock_print.assert_has_calls(chamadas_print, any_order=True)

        # Verifica se o jogo foi finalizado.
        self.assertTrue(self.jogo.jogo_finalizado())

    def teste_de_estresse_do_jogo(self):
        """Teste iterando o jogo várias vezes para ver se algum erro acontece."""

        # inicalizar o jogo
        self.__inicar_jogo()

        quantiade_cartas = '3'
        continuar_jogando = 's'
        encerrar_jogo = 'n'
        # Retorna uma lista entre ['3', 's', 3', 's', 3', 's', 3', 's' ... ] 
        # para continuar jogando, no fim 'n' para sair do jogo.
        side_effect = [ quantiade_cartas if i % 2 != 0 else continuar_jogando for i in range(1, 100) ] + [ encerrar_jogo ]
        with patch('builtins.input', side_effect = side_effect):
            self.jogo.jogar()
        
    def __inicar_jogo(self):
        """Inicia o jogo configurando conforme os requisitos para não ter que repetir
        o código a cada cenário de teste."""

        quantidade_oponentes = '3'
        with patch('builtins.input', return_value = quantidade_oponentes):
            self.jogo.configurar()
            self.jogo.iniciar()

    
    def __jogador(self, id):
        """Retorna um jogador do jogo para realizar cenários testes."""
        return self.jogo._Jogo__jogadores[id]
