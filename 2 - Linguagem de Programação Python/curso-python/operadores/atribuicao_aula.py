# Operadores de atribuição são operadores binários.
# O operador `=` (recebe) é um operador de atribuição:
resultado = 2
print(resultado)    # mostra: 2

resultado = 3   # nova atribuição
print(resultado)    # mostra: 3

# Uma variável pode ser inicializada com um tipo e depois ser reatribuida com um
# novo tipo, permitido assim tipos dinâmicos.
resultado = 'texto'
print(resultado)

# Podemos fazer uma atribuição aditiva.
resultado = 2
resultado += resultado  # `resultado` recebe `resultado` mais `resultado` que é 
                        # igual a 4
resultado += 3 # `resultado` recebe o valor de `resultado` mais 3
print(resultado)    # mostra: 7

# Podemos fazer uma atribuição subtrativa:
resultado -= 1  # resultado = resultado - 1
print(resultado)    # mostra: 6

# Podemos fazer uma atribuição multiplicativa:
resultado *= 4  # resultado = resultado * 4
print(resultado)    # mostra: 24

# Podemos fazer uma atribuição de divisão
resultado /= 2  # resultado = resultado / 2
print(resultado)    # mostra: 12.0

# Podemos fazer uma atribuição do módulo
resultado %= 6  # `resultado`` recebe o resto da divisão de `resultado` dividido 
                # por 6
print(resultado)    # mostra 0.0