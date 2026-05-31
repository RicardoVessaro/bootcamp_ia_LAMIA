from functools import reduce

# Uma lista de dicionários representando alunos.
alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]

# Ao invés de utilizar o `filter` foi utilizado o list comprehension do python
# Estrutura de uma list comprehension:
# [ <expressão do que sera retornado> for <variável laço> in <lista> ]
# Podemos adicionar um teste (`if`):
# [ <expressão do que sera retornado> for <variável laço> in <lista> if <expressao lógica> ]
alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7 ]
print(alunos_aprovados)

# Definido dois parâmetros na lambda (`a` e `b`).
somar = lambda a, b: a + b

# Convertendo a lista de dicionário em uma lista de números.
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]
total = reduce(somar, notas_alunos_aprovados, 0)

print(list(notas_alunos_aprovados)) # mostra: [7.2, 8.1, 8.7]
print(total) # mostra: 24

# Para pegar a média utilizamos o total e a quantidade de alunos aprovados.
print(total / len(notas_alunos_aprovados)) # mostra: 8.0
