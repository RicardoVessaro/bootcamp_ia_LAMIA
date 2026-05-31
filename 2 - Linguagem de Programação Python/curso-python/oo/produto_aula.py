"""
Se a classe `Produto` fosse uma classe vazia poderia utilizar `pass`.
class Produto:
    pass

A classe tem tantoa atributos quanto comportamentos, os comportamentos são 
definidos pelos métodos. Métodos são funções que pertencem a classes.
"""
class Produto:
    # A função especial `__init__` é o construtor da classe, utilizado para
    # inicializar um novo objeto. No python trabalha o conceito de não haver 
    # nada implícito logo utiliza-se o primeiro parâmetro para referenciar a 
    # instância do próprio objeto, chamado `self`.
    # Posso ter valores padrão nos parâmetros dos métodos das classes semelhante
    # as funções
    def __init__(self, nome, preco = 1.99, desc = 0):
        # Definindo dinamicamento um atributo dentro da classe utilizando: 
        #   `self.nome`
        # E atribuindo o valor passado por parâmetro (`nome`).
        self.nome = nome
        # Encaspulamento: Em python para tornar atributos privados utiliza-se 
        # `__` como prefixo, assim o atributo somente pode ser acessado utilizando:
        """
            p1 = Produto('produto')
            p1._Produto__preco # instancia._<NomeClasse><atributo>
        """
        self.__preco = preco
        self.desc = desc

    # Para tornar o atributo `preco` visível ele pode ser acessado via property.
    # Este método se torna um getter para o atributo `__preco` podendo realizar
    # processamentos antes de acessá-lo.
    @property
    def preco(self):
        # return f'R$ {self.__preco}'
        return self.__preco

    # Com o decorator `@preco.setter` pode-se definir quais comportamentos 
    # devem ser realizados antes de atribuir o valor ao atributo.
    @preco.setter
    def preco(self, novo_preco):
        # Somente altera o preço com base nas regras definidas
        if novo_preco > 0:
            self.__preco = novo_preco

    # Sempre que haver um método que pertence a instância deve haver a referência
    # para a instância que se define pelo parâmetro `self` (o primeiro parâmetro
    # do método). Ao chamar o método não é informado o parâmetro `self` de maneira
    # explicíta apenas declarado.
    # `@property`: É o que é chamado de `decorator` em python. Ele faz com que 
    # você passe a acessar o método como se fosse um atributo ao invés de método
    # que é retornado a partir de outros atributos do objeto.
    @property 
    def preco_final(self):
        # Através do `self` podemos acessar os valores atribuídos nos atributos
        return (1 - self.desc) * self.__preco
    
    # Não é necessário capsular todos os atributos privados da classe, faça isso
    # conforme a demanda.

# Para instanciar um `Produto`: 
# Instanciado com o valor do atributo `nome` definido dinamicamente.
p1 = Produto('Caneta', 10, 0.1) # Produto.__init__(p1, ... )
p2 = Produto('Caderno', 14, 0.5)

# Em ambos os casos o preço não é alterado por conta da regra definida no 
# `setter`.
p1.preco = -70
p2.preco = -1.99

# Neste caso os valores são alterados
p1.preco = 70.89
p2.preco = 17.99

# Utiliza-se `.` para acessar membros da classe, no caso o membro acessado é o 
# atributo `nome` definido na funcão `__init__` do `Produto`. 
# Outro membro acessado é o método `preco_final` que com o decorator `property`
# ele é chamado como atributo, sendo um valor calculado baseado em outros 
# atributos do objeto
print(p1.nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)
