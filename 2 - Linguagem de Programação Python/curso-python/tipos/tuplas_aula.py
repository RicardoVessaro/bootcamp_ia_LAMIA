# Tuplas não aceitam modificações.
# Para definir tuplas utilize '( )'.
# Tuplas aceitam repetições .
nomes = ('Ana', 'Bia', 'Gui', 'Leo', 'Ana')

print(type(nomes))  # mostra: <class 'tuple'>
print(nomes)    # mostra: ('Ana', 'Bia', 'Gui', 'Leo', 'Ana')

# Para saber se o elemnto está contido na tupla utilize `in` (o mesmo funciona 
# em listas).
print('bia' in nomes)   # mostra: False 
                        # pois `bia` não é um valor na tupla.
print('Bia' in nomes)   # mostra: True
                        # pois 'Bia' é um valor na tupla.

# Podemos acessar os elementos da tupla igual na lista.
print(nomes[0])     # mostra: Ana

# Podemos definir um intervalo de elementos utilizando `[ : ]`, o mesmo pode ser
# feito com listas.
# No caso de [1:2] selecionamos o intervalo a partir do segundo elemento (1)
# até o terceiro elemento (2) sem incluir o terceiro elemento:
print(nomes[1:2])   # mostra: ('Bia',) 
                    # pois a operação utilizando `:` retorna uma nova tupla
# A partir do segundo elemento até quarto elemento sem incluir o quarto:
print(nomes[1:3])   # mostra: ('Bia', 'Gui')
# A partir do segundo elemento sem incluir o último elemento utilizando o `-1`:
print(nomes[1:-1])  # mostra: ('Bia', 'Gui', 'Leo')
# A partir do terceiro elemento em diante:
print(nomes[2:])
# A partir do início até o penúltimo elemento sem considerar o penúltimo:
print(nomes[:-2])

x = ('Bia')     # `x` representa o tipo `str`, importante tomar atenção nisso pois
                # os parêntes também são usados no contexto de uma expressão e 
                # não apenas para definir tuplas.
print(type(x))  # mostra: <class 'str'>
x = ('Bia', )   # Agora x representa uma tupla (`tuple`), note a `,` entre os 
                # parênteses 
print(type(x))  # mostra: <class 'tuple'>

# Para saber o tamanho também utilizamos `len`.
print(len(nomes))   # mostra: 5

# Algumas funcionalidades disponíveis em tuplas também estão disponíveis nas 
# listas.
