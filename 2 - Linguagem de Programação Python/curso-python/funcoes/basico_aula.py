# Para definir uma funcão utilize a palavra reservada `def` em seguida o nome da
# funcão e seus parâmetros.
# Toda a função tem um bloco definido por indentação.
# O parâmetro definido na função é o `nome`, que possui um valor padrão definido 
# como 'Pessoa', o mesmo é definido como o parâmetro `idade`, tornando-os 
# parâmetros opcionais.
def saudacao(nome = 'Pessoa', idade = 20):
    # Utilizar palavra reservada `pass` para criar funções vazias.
    # `\n` para quebra de linha.
    print(f'Bom dia {nome}! \nVc nem parece ter {idade} anos!')

# Essa função acabou sobreescrevendo e não sobrecarregando a função anterior pois
# no python não há sobrecarga de funções ou métodos.
# def saudacao():
#     print('Boa tarde!')

# Utilizar `_` (snake case) como convenção em nomes de função.
# def saudacao_pela_manha():
#     print('Bom dia')

# Se eu executar esse arquivo a partir dele mesmo utilizando:
# python3 basico_aula.py
# O nome dele será `__main__` ao invés do nome do módulo, isso por que foi a 
# partir desse arquivo que o interpretador do python foi chamado.
# print(__name__)

def soma_e_multi(a, b, x):
    # Python tem a precêdencia nas chamadas dos operadores aritméticos, no caso
    # a multiplicação tem prioridade em relação a soma.
    # Para retornar valores da chamada da função utilize a palavra reservada 
    # `return`
    return a + b * x

# Logo você pode encontrar o seguinte: 
if __name__ == '__main__':
    # Nesse caso essa função só vai ser chamada quando o interpretador for 
    # chamado a partir desse arquivo.
    saudacao('Ana', idade=30)
