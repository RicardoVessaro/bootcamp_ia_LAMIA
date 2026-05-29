#!python3

# Podemos percorrer um `for` dentro do outro utilizando um segundo `for` dentro
# do bloco `for` já existente.
pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'Inteligente']
for p in pessoas:
    for a in adjs:
        print(f'{p} é {a}!')    # mostra:
                                # Gui é Sapeca!
                                # Gui é Inteligente!
                                # Rebeca é Sapeca!
                                # Rebeca é Inteligente!
                                # 
                                # Note que todos os elementos de ambas as listas
                                # foram percorridos.

# Para definir blocos como o laço vazio utilize a palavra chave `pass`.
for i in [1, 2, 3]:
    pass

# Podemos pular para a próxima iteração do laço utilizando a palavra chave `continue`.
for i in range(1, 11):
    if i % 2  == 1:  # sempre `0` se for par e `1` quando ímpar
                # neste caso mostra o valor de `i` apenas quando é par pois o 
                # módulo é `0` onde `0` é verificado como falso na expressão,
                # e quando é verdadeiro o bloco é executado chamando o `continue`
                # que faz com que o laço pule para próxima iteração sem mostrar 
                # o resultado de `i`.
                # Utiliza o `== 1` para que fique mas explicíto o código.
        continue
    print(i)

# Podemos interromper o laço utilizando a palavra chave `break`
for i in range(1, 11):
    if i == 5:
        break
    print(i) # mostra: Os valores 1, 2, 3, 4 em seguida o laço é interrompido.

print('Fim')
