b1 = True
b2 = False 
b3 = True

# Uma operação lógica `E`
print(b1 and b2 and b3)  # mostra: False

# Uma operação lógica `OU`:
print(b1 or b2 or b3)   # mostra: True

# Uma operação lógica `OU exclusivo` (`XOR`):
print(b1 != b2) # mostra: True
                # em python não há um operador para `OU excluisvo` logo utiliza
                # a comparação de diferença que é verdadeira caso ambos sejam
                # difenrtes, operação equivalente ao `XOR`.

# `not` negação lógica:
print(not b1) # mostra: False
print(not b2) # mostra: Verdadeiro

print(b1 and not b2 and b3) # mostra: True
                            # todos as três comparações são verdadeiras, note
                            # o `not b2` que resulta em `True`.

x = 3 
y = 4 

# Podemos utilizar operadores lógicos com operadores relacionais, lembre que
# operadores relacionas resultam em valores booleanos.
print(b1 and not b2 and x < y) # mostra: True

# Utiliza-se o conceito de tabela verdade
