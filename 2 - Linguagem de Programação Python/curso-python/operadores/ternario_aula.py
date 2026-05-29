#!python3
# Operador ternário é um operador que possui três operandos.

lockdown = False
grana = 130

# atribui o valor (`Em casa`) se (if) a condição (lockdown) é verdadeira se 
# não (else) `Uhuuu`
# Os três operandos são:
# - `'Em casa'`
# - `lockdown or grana <= 100` # A expressão toda 
# - `'Uhuuuu`
# <resultado quando verdadeiro> if <expressao logica> else <resultado quando falso>.
status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'

print(status)   # mostra: Uhuuuu

print(f'O status é: {status}')  # mostra: O status é: Uhuuuu
                                # o formatador `f'` é suportado apenas no python 3.
