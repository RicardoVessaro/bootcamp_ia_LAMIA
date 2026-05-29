# Convertando o valor informado no `.input` para `float` e atribuindo a variável
# `nota`.
# O python permite utiliza `;` mas não é recomendado.
nota = float(input('Informe a nota do aluno: '));

# comportado recebe verdadeiro apenas se for informado `'s'` no terminal
comportado = True if input('Comportado (s/n): ') == 's' else False

# Conceito de bloco em python.
# O bloco é definido pela indentação (tab). Um bloco é um conjunto de sentenças 
# juntos. 
# Executa o bloco se a condição for verdadeira.
# Note que `comportado` é uma variável booleana ao invés de uma expressão lógica.
if nota >= 9 and comportado: 
    # Bloco para quando a condição é verdadeira. 
    print('Duas palavras: para bens! :P')
    print('Quadro de Honra')
elif nota >= 7: # `elif` é utilizado quando há outra condição para verificar
                # caso a condição do bloco anterior seja falsa. 
    print('Aprovado')
elif nota >= 5.5: # outros blocos `elif` podem ser utilizados antes do `else`
    print('Recuperação')
elif nota >= 3.5: # apenas o primeiro bloco que atende a condição será executado 
                # os demais não são executados
    print('Recuperação + Trabalho') # python 2 pode apresentar erro por conta do 
                                    # enconding quando há acentos
else : # O bloco `else` é executado quando a condição de `if` é falsa.
    print('Reprovado')
# Esse trecho de código está fora do bloco por estar em outra indentação.
print(nota) # mostra o input informado no terminal
