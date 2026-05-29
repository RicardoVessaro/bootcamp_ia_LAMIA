# `while` é utilizado para representar uma quantidade indeterminada de 
# repetições, nesse caso apenas sairá do bloco `while` quando o valor de 
# `x` for igual a `-1`. Enquanto a expressão do `while` é verdadeira o bloco 
# dentro dele é executado.
x = 0
while x != -1:
    x = float(input('Informe o número ou -1 para sair: ' ))

print('Fim!')

# Neste caso as notas são informadas no terminal e sendo somadas na variável 
# `total`, quando for informado `-1` sai do programa e mostra a média das notas
# informadas com base na quantidade de notas informadas e na soma das notas.
total = 0
qtde = 0
nota = 0
while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    # A nota é apenas válida se for diferente da condição de saída que no caso 
    # é -1.
    if nota != -1:
        qtde += 1
        total += nota

# print(f'A média da turma é  {total / qtde}')

# Também pode se utilizar o `while` para uma quantidade determinada de iterações.
# Em uma situação como essa podemos utilizar o `for` ao invés do `while`.
x = 10 
while x:    # Lembre-se que `0` é verficado como falso, logo quando `x` chegar a 
            # zero o bloco `while` não é mais executado.
    print(x)
    # `x` vai sendo decrementado de 1 em 1.
    x -= 1

print('Fim!')
