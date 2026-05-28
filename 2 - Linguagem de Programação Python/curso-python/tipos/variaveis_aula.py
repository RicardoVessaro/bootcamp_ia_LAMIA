# Para declarar uma variavel utilize:
# <nome_variavel> = <valor>
# exemplo: váriavel a recebe (=) valor de 3.
a = 3

b = 4.4

# para soma utilize: `+`:
print(a + b)

# para declarar variaveis de texto utilize áspas simples ('') ou áspas duplas ("").
texto = 'Sua idade é...'
idade = 23

# Nao é possivel concatenar `str` (string) com `int` (inteiro)
# print(texto + idade).

# Pode converter a variavel `int` em `str` utilizando `str()` mas segundo o 
# video não é recomendado:
# print(texto + str(idade))

# Com `f''` (f + str) podemos interpolar os valores (interpretar variaveis de 
# fora do texto dentro do texto):
print(f'{texto}')   # mostra: Sua idade é...

print(f'{texto} {12 + 13}') # mostra: Sua idade é... 25

print(f'{texto} {idade}')   # mostra: Sua idade é... 23

# Nao é possivel concatenar int com str utilizando `+` mas podemos multiplicar 
# uma `str` utilizando `*`
print(3 * 'bom dia ') # mostra: bom dia bom dia bom dia

saudacao = 'bom dia '
print(3 * saudacao) # mostra: bom dia bom dia bom dia

# Em python não há constantes mas existe uma convencao utilizando letras 
# maiúsculas, não é garantia que isso é uma constante, o python não interpreta 
# como constante.
PI = 3.14
PI = 3.1415

# Input mostra o texto informado no terminal e em seguida espera que um valor 
# seja informado no terminal para que o código prossiga, nesse caso o valor é 
# atruibuído a variável `raio`.
# `input` retorna uma váriavel do tipo `str` para converte-lá em `float` utilize a 
# função built-in `float()`
# `float`: é o tipo do numéro com ponto flutuante (casas decimais)
raio = float(input('Informe o raio da circ? '))

# Para saber o tipo de uma variável utilize a função built-in `type()`
print(type(raio)) # mostra: <class 'str'>, agora mostra: <class 'float'>

# `area` recebe `PI` vezes o `raio` ao quadrado (`raio` vezes `raio`)
# area = PI * raio * raio
# a função built-in `pow` permite fazer a operação de potência.
area = PI * pow(raio, 2)    # area recebe `314.15000000000003`
                            # note a questão do arredondamento residual
                            # isso acontece em linguages que utilizam o ponto
                            # flutuante ao invés do valor exatamente preciso
                            # por utilizar um algoritmo muito mais rápido 
print(area) # mostra: 314.15000000000003
print(f'A área da circ é {area} m2.') # mostra: A área da circ é 314.15000000000003 m2.
