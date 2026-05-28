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
Este bloclo definido entre 3 áspas duplas pode ser utilizado tanto quanto uma 
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
import operadores.ternario_aula