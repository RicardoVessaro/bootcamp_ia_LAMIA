from functools import reduce

# Uma lista de dicionários representando alunos
alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]

# Utiliza a palavra reservada `lambda` para funções de uma única linha conhecidas
# também como funções anônimas. Essa função é atribúida a uma variável, para que
# possa ser utilizada depois.
# Estrutura da `lambda`:
# lambda <parâmetros> : <expressão que será retornada>
# `lambda`s sempre teram uma expressão que retorna algum valor, no caso 
# `aluno_aprovado` retorna `True` or `False`
aluno_aprovado = lambda aluno: aluno['nota'] >= 7
# Lambda para filtrar outros alunos
aluno_honra = lambda aluno: aluno['nota'] >= 9

# `filter` é a função utilizada para filtrar dados de uma lista caso a expressão
# lógica definida seja verdadeira. `filter` recebe a função que será utilizada
# `aluno_aprovado` e a lista percorrida para gerar a lista filtrada (`alunos`).
alunos_aprovados = filter(aluno_aprovado, alunos)

# Utilizado o `list` para converter o `filter` object e verificar os alunos 
# aprovados. 
# print(list(alunos_aprovados))   # Alunos que tema. nota menor que 7 não estão 
#                                 # na lista. E note que a lista orginal não foi
# print(alunos)                   # alterada. Pois o resultado do fitro devolve 
                                # uma nova estrutura mantendo a lista informada
                                # inalterada.

# alunos_honra = filter(aluno_honra, alunos)
# print(list(alunos_honra))   # mostra: []
                            # nenhuma chamada da função retornou verdadeiro, 
                            # portanto a lista está vazia.

# Agora utilizar funções lambdas para retornar apenas o valor da nota do aluno
# tranformando o dicionário em uma nota.
obter_nota = lambda aluno: aluno['nota']

# Definido dois parâmetros na lambda (`a` e `b`)
somar = lambda a, b: a + b

# Também pode chamar a função lambda sem necessariamente utilizar `reduce` ou 
# outra função que receba uma função por parâmetro.
# print(obter_nota(alunos[2])) # mostra: 8.7

# Buscando apenas as notas dos alunos aprovados, alunos aprovados são recuperados
# a partir do `filter` aplicado anteriormente.
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))
total = reduce(somar, notas_alunos_aprovados, 0)

print(list(notas_alunos_aprovados)) # mostra: [7.2, 8.1, 8.7]
print(total) # mostra: 24

# Para pegar a média utilizamos o total e a quantidade de alunos aprovados.
print(total / len(notas_alunos_aprovados)) # mostra: 8.0
