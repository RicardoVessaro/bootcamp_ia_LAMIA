# Operadores aritméticos são operados binários, operadores binários operam em
# dois operandos. 
# As operações podem ser feitas em variáveis ou valores literais.

x = 10 
y = 3

# Operadores aritméticos operam na chamada sintaxe in fix:
# `+x` prefix
# `x++` postfix
# `x + y` infix
# `+` opera em `x` e `y`.
print(x + y)    # soma, mostra: 13
print(x - y)    # subtração, mostra: 7
print(x * y)    # multipicação, mostra: 30
print(x / y)    # divisão, mostra: 3.3333333333333335
print(x % y)    # módulo, mostra: 1
                # módulo é o resto da divisão.

# Em operações aritméticas `int` com `float` o resultado é `float`.

# `%` módulo é muito utilizado para determinar se o número é par ou ímpar:
par = 34
impar = 33

# `==` é um operador relacional que faz a comparação.
print(par % 2 == 0) # mostra: True
print(impar % 2 == 1)  # mostra: True
