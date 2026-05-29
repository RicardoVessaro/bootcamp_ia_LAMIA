

print (not 'valor') # mostra: False
                    # pois `valor` é considerado como verdadeiro
                    # e está sendo negado com `not`

print(not not 'valor')  # mostra: True 
                        # pois `valor` é considerado como verdadeiro
                        # e está sendo negado com `not` duas vezes

# No caso de `if a:` e no `print(not 'valor')`
# O python considera `a` como verdadeiro ao invés de uma expressão relacional.
a = 'valor'
if a:
    # Cai nesse bloco
    print('Existe')
else:
    print('Não existe ou zero ou vazio...')

# Qualquer número diferente de `0` é avaliado como verdadeiro apenas o `0` é 
# considerado falso.
a = 0
if a:
    print('Existe')
else:
    # Cai nesse bloco.
    print('Não existe ou zero ou vazio...')

a = -0.00001
if a:
    # Cai nesse bloco.
    print('Existe')
else:
    print('Não existe ou zero ou vazio...')

# Uma `str` (string) vazia é avaliado como falso.
a = ''
if a:
    print('Existe')
else:
    # Cai nesse bloco.
    print('Não existe ou zero ou vazio...')

# Uma `str` (string) com espaços em branco é avaliado como verdadeiro.
a = ' '
if a:
    # Cai nesse bloco.
    print('Existe')
else:
    print('Não existe ou zero ou vazio...')


# Uma lista vazia também é considerado como falso.
a = []
if a:
    print('Existe')
else:
    # Cai nesse bloco.
    print('Não existe ou zero ou vazio...')

# Um conjunto vazio também é considerado como falso.
a = {}
if a:
    print('Existe')
else:
    # Cai nesse bloco.
    print('Não existe ou zero ou vazio...')

# No `if` não necessariamente é informado uma expressão relacional
