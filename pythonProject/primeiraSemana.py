#aceita uma lista como entrada e troca o primeiro e o último elementos da lista
def troca_primeiro_ultimo(lista):
    lista[0], lista[-1] = lista[-1], lista[0]
    return lista

lista_de_compras = ['melancia', 'uva', 'banana', 'maçã']
print(troca_primeiro_ultimo(lista_de_compras))