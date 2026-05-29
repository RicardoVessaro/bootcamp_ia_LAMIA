#!python3
# `#!python3` é um `shebang`: comentário utilizado em scripts para que o 
# interpetador entenda qual runtime utilizar, no caso o python3.

# Utilizado a extensão run code do vscode para executar os scripts, interessante
# para entender como funciona dessa forma, para executar o arquivo diretamente
# utilize: 
# Ctrl+Alt+N (Ctrl+Opt+N) 
#
# Para executar o script posso utilizar:
# python3 main_aula.py

# print('Bem vindo!')   # mostra: Bem vindo!

# Normalmente a importação fica no inicio do arquivo mas isso não é obrigatório 
# em python:
# import pacote.sub.arquivo_aula

# print(__name__)   # mostra: __main__ 
                    # sendo este o módulo main e não algum módulo referente ao script.
# print(__package__)    # mostra: None 
                        # indicando que não há pacote.

"""
Este bloco definido entre 3 áspas duplas pode ser utilizado tanto quanto uma 
String (considerando quebra de linhas)
como também comentário em múltiplas linhas, diferente do utilizando sustenido (#)
em várias linhas como anteriormentes.
"""

# import tipos.variaveis_aula

# Pode utilizar a palavra chave `from` para importar determinados módulos do 
# pacote ao invés de importar tudo de uma vez.
# carregando assim primeiro o módulo `variaveis_aula` e depois `basicos_aula`
# from tipos import variaveis_aula, basicos_aula
# import tipos.lista_aula
# import tipos.tuplas_aula
# import tipos.conjuntos_aula
# import tipos.dicionarios_aula

# import operadores.unarios_aula
# import operadores.aritmeticos_aula
# import operadores.relacionais_aula
# import operadores.atribuicao_aula
# import operadores.logicos_aula
# import operadores.ternario_aula

# import controle.if_1_aula
# import controle.if_2_aula
# import controle.for_1_aula
# import controle.while_1_aula
# import controle.outros_exemplos_aula

# Traz as funções de `basico_aula` do pacote `funcoes` para o espaço de nome
# (`name space`) do script em questão, para que assim as funções definidas no 
# módulo `funcoes` estejam disponíveis (vísiveis) neste script.
from funcoes import basico_aula
# Acessa e chama a função `saudacao` através do módulo `basico_aula`.
basico_aula.saudacao()

# Podemos também utilizar:
# from funcoes.basico_aula import saudacao
# Assim também trazemos a função para o name space mas importamos diretamente o 
# módulo `basico_aula` que está em `funcoes`. Mas lembre-se que caso neste script
# também tenha uma função chamada `saudacao` isto irá gerar conflito.
# saudacao()

# Podemos chamar passando apenas o parâmetro por ordem.
basico_aula.saudacao('Maria')
# Nenhum parâmetro uma vez que todos os parâmetros possuem valor padrão.
basico_aula.saudacao()
# Informando os dois parâmetros seguidos pela ordem definida.
basico_aula.saudacao('João', 33)
# Caso queira passar apenas um parâmetro específico podemos defini-lo na chamada.
basico_aula.saudacao(idade=89)
# Lembrando que em python não a sobrecarga de métodos.

# Ao fazer a chamada da função podemos mudar a ordem dos parâmetros utilizando os
# parâmetros nomeados, mesmo que na definição do parâmetro não haja valor padrão 
# O retorno da função chamada será armazeanda na variável `a`.
# A váriavel `a` é diferente da váriavel `a` da função pois cada um está 
# associada a um escopo (bloco) e name space diferente.
a = basico_aula.soma_e_multi(x=10, a=2, b=3)
# É mais flexível ter funções que retornam dados do que mostrem eles através
# de `.print`, assim podemos utilizar as informações retornadas da forma que 
# prefer, seja mostrando no terminal, seja utilizando para outro processamento,
# etc.
b = basico_aula.soma_e_multi(x=20, a=3, b=7)
print(a) # mostra: 32

resultado = a + b 
print(resultado) # mostra: 175
