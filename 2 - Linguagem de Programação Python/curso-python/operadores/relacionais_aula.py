# Operadores relacionais são operadores binários.
# O resultado de operações relacionais sempre será booleano: Verdadeiro (True)
# ou falso (False).
x = 7
y = 5

print(x > y)    # maior que, mostra: True
print(x >= y)   # maior ou igual a, mostra: True
print(x < y)    # menor que, mostra: False
print(x <= y)   # menor igual a, mostra: False
print(x == y)   # igual a, mostra: False
print(x != y)   # diferente de, mostra: True

# Note que ao comparar se '5' (`str`) e 5 (`int`) são diferentes o resultado é 
# verdadeiro pois python considera os tipos
print('5' != 5) # mostra: True