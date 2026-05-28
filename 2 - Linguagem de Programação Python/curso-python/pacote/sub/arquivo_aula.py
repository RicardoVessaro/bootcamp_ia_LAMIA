# print('Funcionou')
# A váriavel `__name__` retorna o nome do módulo e do pacote referente ao script, 
# ex: 
# pacote.sub.arquivo_aula
print(__name__)

# `__package__` para o nome do pacote referente ao script:
# pacote.sub
print(__package__)

# As variáveis apresentadas: `__name__` e `__package__` são chamadas de 
# variáveis built-ins disponíveis pelo python.
# Há também funções built-in com por exemplo `abs()` utilizado para pegar um 
# valor absoluto.
print(abs(-321))

# Váriaveis e funcões built-in estão disponíveis em todos os lugares no script 
# python.
