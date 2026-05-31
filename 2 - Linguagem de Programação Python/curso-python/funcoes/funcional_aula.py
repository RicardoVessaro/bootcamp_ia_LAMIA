# Aspectos da programação funcional em python
def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

# Podemos atribuir uma função dentro de uma variável
somar = soma
# Em seguida podemos chamar essa variável
print(somar(3, 4)) # mostra: 7

# Essa função recebe uma função por parâmetro
def operacao_aritmetica(fn, op1, op2):
    # A função passada por parâmetro é chamada e os operadores são passados 
    # como parâmetro.
    return fn(op1, op2)

# A operação chamada será a passada no primeiro parâmetro, nesse caso `soma`
resultado = operacao_aritmetica(soma, 13, 48)
print(resultado) # mostra: 61

# Aqui `operacao_aritmetica` chama a função `sub`
resultado = operacao_aritmetica(sub, 13, 48)
print(resultado) # mostra: 35

# Funções passadas como parâmetro são muito utilizadas em `map` e `reduce`

# Uma função pode chamar outra função.
def soma_parcial(a):
    # A função `concluir_soma` é definidade no escopo da função `soma_parcial`.
    def concluir_soma(b):
        return a + b
    return concluir_soma # note que a função não está sendo chamada

# `fn` recebe a função `concluir_soma` definida em `soma_parcial` onde o valor 
# 10 será acessado internamente referente ao argumento `a`.
fn = soma_parcial(10)

# Agora a função `concluir_soma` definida em `soma_parcial` é chamada operando
# a soma com os operandos `10` definido na chamada `soma_parcial(10)` e o 12
# definido na chamda de `fn`.
resultado_final = fn(12) 
print(resultado_final) # mostra: 22

# Isso pode ser chamado em uma única linha onde quando a primeira função já 
# retorna é possível chamar o retorno em seguida. 
# `10` é o parâmetro da função `soma_parcial`
# `12` é o parâmetro da função retornada.
resultado_final = soma_parcial(10)(12)
print(resultado_final) # mostra: 22

"""
Esse uso é visto para tornar a execução final tardia, dividir o processamento
em partes como exemplificado: 

def soma_total(a, b):
    - processamento 1 que depende de `a`, demora 10 segundos
    - processamento 2 que depende de `a`, demora 10 segundos
    - processamento 3 que depende de `a`, demora 40 segundos
    - processamento que utiliza `b` e demora 10 segundos
    No fim utiliza `b` para a operação que utiliza ambos os parâmetros
    return a + b 

r1 = soma_total(1, 1) # chamada que demora 1m10s
r2 = soma_total(1, 2) # chamada que demora 1m10s
r3 = soma_total(1, 3) # chamada que demora 1m10s

No fim foram 3m30s de processamento.

Se parcializarmos essa operação podemos diminuir o tempo de processamento.
def soma_parcial(a):
    - processamento 1 que depende de `a`, demora 10 segundos
    - processamento 2 que depende de `a`, demora 10 segundos
    - processamento 3 que depende de `a`, demora 40 segundos
    Após todos os processamentos realizados com `a` serem feitos utilizamos o 
    segundo argumento definindo-o como argumento na função que será retornada
    def concluir_soma(b):
        - processamento que utiliza `b` e demora 10 segundos
        return a + b 
        No fim utiliza `b` para a operação que utiliza ambos os parâmetros
    return concluir_soma

soma_parcial_1 = soma_parcial(1) # chamada que demora 1m
r1 = soma_parcial_1(1) # chamada que demora 10s
r2 = soma_parcial_1(2) # chamada que demora 10s
r3 = soma_parcial_1(3) # chamada que demora 10s

Desta mandeira todo o processamento custos é tratado na única chamada feita em:
soma_parcial_1 = soma_parcial(1)
E os demais processamentos que dependen do primeiro parâmetro já tem o resultado 
definido na chamada da função retornada (`concluir_soma(b)`), logo:
    soma_parcial_1(1)
não precisa fazer todo o processamento que demora 1m a cada chamada.

Neste exemplo podem ser notados principios da programação funciona como lazy. 
"""

soma_1 = soma_parcial(1)
r1 = soma_1(2)
r2 = soma_1(3)
r3 = soma_1(4)
print(resultado_final, r1, r2, r3) # mostra: 22 3 4 5
