
# Para definir um dicionário utilize ` { 'chave' : <valor> } ` no caso foi 
# definido um dicionário utilizando as chaves: `'nome', 'nota', 'ativo'`.
aluno = {
    'nome': 'Pedro Henrique',
    'nota': 9.2,
    'ativo': True
}

print(type(aluno))  # mostra: <class 'dict'>

# A partir da chave do dicionário podemos acessar os valores utilizando ['chave'].
print(aluno['nome'])    # mostra: Pedro Henrique
print(aluno['nota'])    # mostra: 9.2
print(aluno['ativo'])   # mostra: True

# Ao utilizar `len` no dicionário ele mostra quantos pares e valores possui.
print(len(aluno))   # mostra: 3
