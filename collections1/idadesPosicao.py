idades = [15, 87, 65, 56, 32, 49, 37]

for idade in range(len(idades)):  # range passa pela lista
    print(idade, idades[idade])


print(list(range(len(idades))))  # cria uma lista com as posições
print(list(enumerate(idades)))  # cria uma lista com tuplas de posição e idade

for valor in enumerate(idades):
    print(valor)

for indice, idade in enumerate(idades):  # unpacking da tupla
    print(indice, "-", idade)

print(sorted(idades))  # ordena as idades da lista
print(sorted(idades, reverse=False))
print(sorted(idades, reverse=True))  # ordem decrescente
print(list(reversed(sorted(idades))))
print(list(reversed(idades)))  # coloca a lista ao contrário

idades.sort()  # função que ordena a lista
print(idades)  # https://docs.python.org/3/tutorial/datastructures.html

nomes = ["fulano", "Sicrano", "Beltrano"]
print(sorted(nomes))  # sorted põe minúsculos depois de maiúsculos


usuarios = [
    ("Fulano", 38, 1981),
    ("Sicrano", 32, 1987),
    ("Beltrano", 40, 1979)
]

for nome, idade, nascimento in usuarios:  # forma de desempacotar e trazer apenas o item que vc quer
    print(nome)

for nome, _, _ in usuarios:  # outra forma não mt interessante pois não é claro de que se tratam os outros elementos
    print(nome)
