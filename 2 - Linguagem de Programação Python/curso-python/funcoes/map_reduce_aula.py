# O `reduce` não é uma função built in do python devemos importa-lá do pacote
# `functools`
from functools import reduce

notas = [6.4, 7.2, 5.8, 8.4]

# Somando o valor em cada elemento de `notas` de forma procedural.
# Utilizando a função built in `enumerate` podemos retornar o indíce da lista 
# atribuido a `i` e seu elemento atribuído em `nota`
# for i, nota in enumerate(notas):
#     # print(i, nota)  # mostra:
#                         # 0 6.4
#                         # 1 7.2
#                         # 2 5.8
#                         # 3 8.4
#     notas[i] = nota + 1.5
# print(notas) # mostra: [7.9, 8.7, 7.3, 9.9]

# Outra forma de fazer
# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5
# print(notas) # mostra: [7.9, 8.7, 7.3, 9.9]

# Utilizado o `map`
# `map`: Função que vai pegar a lista informada, fazer uma segunda lista do 
# mesmo tamanho com a lista informada mapeada.

# Função que será informada no `map`
def mais_um_meio(nota):
    return nota + 1.5

# Ao utilizar o `map` tranforma uma lista em outra lista atráves dos valores 
# percorridos na lista informada.
notas_finais = map(mais_um_meio, notas)
# print(list(notas_finais))   # mostra: [7.9, 8.7, 7.3, 9.9]
                                # # para que mostre os resultados converti o 
                                # `map` object retornado da função `map` em uma 
                                # lista.

# Podemos utilizar a programação funcional para tal.
def somar_nota(delta):
    # Neste exemplo `nota` será apenas utilizado pelo `map` acessando a função 
    # `somar` ao fazer o mapeamento para gerar a nova lista.
    def somar(nota):
        return nota + delta
    return somar

notas = [6.4, 7.2, 5.4, 8.4]
# Dessa maneira a função retornada de `somar_nota` é utilizada como parâmetro
# para a função `map`.
notas_finais_1 = map(somar_nota(1.5), notas)
notas_finais_2 = map(somar_nota(1.6), notas)

print(list(notas_finais_1))   # mostra: [7.9, 8.7, 6.9, 9.9]
                                # # para que mostre os resultados converti o 
                                # `map` object retornado da função `map` em uma 
                                # lista.

print(list(notas_finais_2))   # mostra: [8.0, 8.8, 7.0, 10.0]
                                # # para que mostre os resultados converti o 
                                # `map` object retornado da função `map` em uma 
                                # lista.

# Agora somando todas as notas dos alunos.

# De maneira procedural:
# total = 0
# for n in notas:
#     total += n 
# print(total) # mostra: 27.4

# De maneira funcional podemos utilizar o `reduce`.
# Função que será utilizada pelo `reduce`. Ao ser utilizada pelo reduce o 
# primeiro parâmetro é o acumulador e o segundo parâmetro o atual
def somar(a, b):
    return a + b

# Ao utilizar o `reduce`: 
# - O primeiro parâmetro é a função a ser executada (`somar`); 
# - O segundo parâmetro a lista (`notas`)
# - O terceiro parâmetro o valor inicial (`0`).
total = reduce(somar, notas, 0)
print(total) # mostra: 27.4
