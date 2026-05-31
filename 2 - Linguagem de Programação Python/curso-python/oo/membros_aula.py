# A níveis de membros em uma classe em python, são eles:
# - estático
# - classe
# - instância


class Contador:
    contador = 10    # Este aqui é um atributo de classe. 
                    # Um atributo a nível de instância é definido pelo `self`
                    # no método `__init__`

    # Não referencie atributos de classe utilizando a instância como é o caso em:
    #   self.contador += 1
    def inc_maluco(self):
        # Pois não há o atributo `contador` na instância do objeto, assim ele 
        # busca uma referência a nível de classe que no caso é `contador` ao 
        # utilizar `self.contador + 1` dessa maneira é atribuido o valor 
        # definindo assim um atributo a nível de instância através do 
        # `self.contador = ...` fazendo com que nas próximas chamadas de 
        # `inc_maluco` a referência agora seja o atributo da própria instância, 
        # sendo dois valores diferentes, por isso ao acessar `Contador.inc()` 
        # ele vai acessar a refêrencia do nível de classe então cuidado.
        self.contador = self.contador + 1 
        return self.contador

    def inst(self):
        return 'Estou bem!'

    # Para manipular atributos de classe utilizamos um método decorado com 
    # `@classmethod`.
    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador
    
    # Neste caso decrementando o valor
    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador
    
    # Para definir um método estático utiliza o decorator `@staticmethod`
    @staticmethod
    def mais_um(n):
       return n + 1
    

# A partir de uma instância é possível acessar um método de classe. Para ter uma
# instância é necessário a classe, ou seja a classe sempre vai existir por isso 
# é possível acessar o nível de classe a partir da instância.
c1 = Contador()
print(c1.inc())
print(c1.inc())
print(c1.inc())
print(c1.dec())
print(c1.dec())
print(c1.dec())

# Para acessar ao nível de classe não há necessidade de uma instância, desta 
# forma ele é acessado a partir da instância.
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
# Mas não é possível acessar um método (membro) do nível instância.
# Neste caso precisa haver uma instância: 
# print(Contador.inst())

c1 = Contador()
# Assim acessamos o método de instância através da instância.
print(c1.inst())

# Tome cuidado, 
                        # Mostra a nível de instância:
print(c1.inc_maluco())  # 11
print(c1.inc_maluco())  # 12
print(c1.inc_maluco())  # 13
print(c1.inc_maluco())  # 14
                        # Em seguida mostra a nível de classe:
print(Contador.inc())   # 11
print(Contador.inc())   # 12

# Método estático acessado atráves da classe.
print(Contador.mais_um(99))
