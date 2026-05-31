class Carro:
    def __init__(self):
        # Atributo definido por padrão ao inicializar a o objeto.
        self.__velocidade = 0

    # getter para o atributo que é manipulado internamente.
    @property
    def velocidade(self):
        return self.__velocidade

    # Manipula o atributo privado aumentando o valor de `__velocidade`.
    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade
    
    # Manipula o atributo privado diminuindo o valor de `__velocidade`.
    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade

# Herança em python é definida pelos parênteses e a classe informada, neste caso
# a classe `Uno` herda a classe `Carro`:
class Uno(Carro):
    # Utilizando `pass` para classe vazia.
    pass

class Ferrari(Carro):
    pass

    # Desta forma sobreescrevemos o comportamento modelado no método `acelerar`.
    def acelerar(self):
        super().acelerar()
        return super().acelerar()

# Manipula a velocidade do carro através dos métodos modelados. 
c1 = Uno()
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())
print(c1.frear())

# Note que por sobreecrever o método `acelerar` o valor no atributo `__velocidade`
# muda.
c1 = Ferrari()
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())
print(c1.frear())
