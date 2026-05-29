#!python3 

# A função built-in `range()` retorna valores até o intervalo (exclusivo)
# `range(10)` retorna o intervalo de [1, 10[ (10 exclusivo, não contido no 
# intevalo).
# `for` percorre todos os valores no (`in`) intervalo de 1 a 9 atribuindo os 
# valores na váriavel `i`.
for i in range(10):
    print(i, end=' ')

# `print` apenas para quebrar a linha
print('')

# Por padrão o `range()` começa do zero mas em `range(1, 11)` definimos o início
# em `1`
for i in range(1, 11):
    print(i, end=' ') # mostra os valores do intervalo [1,11[ ou [1,10]

print('')

# Podemos também definir o passo, neste caso será percorrido o intervalo de 
# [1, 100[ de 7 em 7, o que seria (1, 8, 15, 22... 99).
for i in range(1, 100, 7):
    print(i, end=' ')

print('')

# Neste caso o intervalo começa no `20` e vai até `0` de 3 em 3 o que seria:
# (20, 17, 14, 11 ... 2)
for i in range(20, 0, -3):
    print(i, end=' ')

print('')

# Utilizando `for` também podemos percorrer valores em uma lista.
nums = [2, 4, 6, 8]
for n in nums: # `n` recebe o valor de um elemento da lista a cada iteração.
    # Podemos alterar o print para que ao invés de quebrar a linha `\n` colocar 
    # um espaço e assim mostrar todos os numeros na mesma linha no terminal.
    print(n, end=' ') # mostra: 2 4 6 8 %

print('')

# Podemos também percorrer uma `str`.
texto = 'Python é muito massa!'
for letra in texto:
    print(letra, end=' ') # mostra: P y t h o n   é   m u i t o   m a s s a ! %  

print('')

# Podemos também percorrer um conjunto.
for n in {1, 2, 3, 4, 4, 4} :
    print(n, end=' ') # mostra: 1 2 3 4 %

print('')

produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}

# No dicionário `atrib` recebe o atributo (chave) do dicionário.
for atrib in produto:
    # Acessa o valor a partir da chave (`atrib`).
    print(atrib, '==>', produto[atrib], end=' ')   # mostra:
                                            # nome ==> Caneta
                                            # preco ==> 8.8
                                            # desc ==> 0.5

print('')

# A outra forma de percorre o dicionário é utilizar o método `.items()`:
for atrib, valor in produto.items():
    print(atrib, '==>', valor, end=' ')  # mostra:
                                # nome ==> Caneta
                                # preco ==> 8.8
                                # desc ==> 0.5

print('')

# Para percorrer apenas o valor utilize `.values()`:
for valor in produto.values():
    print(valor, end=' ') # mostra: Caneta 8.8 0.5 %

print('')

# Para percorrer apenas as chaves também podemos utilizar `.keys()`:
for atrib in produto.keys():
    print(atrib, end=' ') # mostra: nome preco desc %  

print('')
