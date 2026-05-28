# Para definir listas utilize '[ ]'.
# Variável `nums` recebe uma lista com os valores 1, 2 e 3.
nums = [1, 2 , 3]
print(type(nums)) # mostra: <class 'list'> representando uma lista
# Os tipos basicos e tipo `list` são classes que serão vistas mais pra frente.

# `.append` adiciona um elemento na lista
nums.append(3)
nums.append(4)
nums.append(500)
# Função built-in `len` é utilizada para saber o tamanho de alguma variável como 
# no caso da lista.
print(len(nums)) # mostra: 6

# `in` também funciona nas tuplas.
print(2 in nums) # mostra: True pois 2 está contido na lista `nums`

# A lista começa a partir do índice 0.
# Podemos acessar um elemento da lista através do índice utilizando `[ ]`:
nums[3] = 100 # atribui o valor 100 no quarto elemento da lista
# Também pode se utilizar o `.insert(indice, objeto)`.
nums.insert(0, -200) # insere o valor `-200` no primeiro elemento da lista

# Mostra o sétimo elemento da lista.
print(nums[6]) # mostra: 500

# Uma forma de pegar o ultimo elemento é utilizando o `-`.
# Utilize [-1] para buscar o último elemento:
print(nums[-1]) # mostra: `500`

# Mostra o penúltimo elemento da lista:
print(nums[-2]) # mostra: 4

# Para mostrar os valores da lista: 
print(nums) # mostra: [-200, 2, 3, 100, 4, 500]

# Algumas funcionalidades disponíveis em listas também estão disponíveis nas 
# tuplas.
