# Para definir um conjunto utilize `{ }`.
print({1, 2, 3})
print(type({1, 2, 3}))  # mostra: <type 'set'>
conj = {1, 2, 3, 3, 3, 3, 3}
print(conj) # mostra: {1, 2, 3} 
            # pois conjuntos não aceitam elementos repetidos.

# Um `set` (conjunto) não suporta acesso por indíce por não ser indexado.
# print(conj[1]) # esta linha lança um erro

# Podemos recuperar o tamanho do conjunto também utilizando `len`.
print(len(conj))    # mostra: 3
