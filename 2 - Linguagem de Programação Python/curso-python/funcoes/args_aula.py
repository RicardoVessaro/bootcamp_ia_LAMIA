# PEP
# Python EnxEnhancement Proposal
# São guias de estilo de codificação do python como:
# - Utilizar espaços ao invés do tab
# - 2 linhas após cada função
# - Última linha do arquivo em branco

# Pode colocar qualquer nome para o `args`, ex: `args`, `nums`, etc.
# Neste caso `nums` são parâmetros posicionais
def soma(*nums): 
    # print(type(nums)) # mostra: <class 'tuple'>
    # Percorre os argumentos (`*nums`) informado na função e atribui a soma na 
    # variável `total`.
    total = 0 
    for n in nums:
        total += n
    return total

# Nesta função recebe como parâmetro o keyword args, argumentos que são nomeados
# recebendo um dicionário em `kwargs`.
def resultado_final(**kwargs):
    # print(type(kwargs)) # mostra: <class 'dict'>
    # Acessamos o valor pela chave por se tratar de um dicionário, a chave é 
    # definida pelo parâmetro nomeado que foi informado ao chamar a função. 
    # print(kwargs['nome']) 
    # print(kwargs['nota'])
    status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado(a)'
    # Utiliza áspas duplas para referencias o valor do tipo `str` quando está 
    # na interpolação definida em f'{...}.
    return f'{kwargs["nome"]} foi {status}'
