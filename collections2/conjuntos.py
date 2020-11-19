# duas listas possuem elementos repetidos:

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram_cursos = usuarios_data_science.copy()  # copy cria uma cópia rasa dos dados (uma referência, apenas)
# outra forma:
# assistiram_cursos = []
assistiram_cursos.extend(usuarios_machine_learning)  # extend coloca dentro da lista
print(assistiram_cursos)  # https://docs.python.org/3/tutorial/datastructures.html

set(assistiram_cursos)  # transforma em conjunto: SEM elementos repetidos, mas sem indexação
print(assistiram_cursos)

conjunto = set ([1,2,3,1])
print(conjunto)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# resolvendo indexação em um conjunto:
for usuario in set(assistiram_cursos):
    print(usuario)

# OPERAÇÕES DE CONJUNTOS:
print(usuarios_machine_learning | usuarios_data_science)  # opção ao .extend (une os dois CONJUNTOS, apenas)
print(usuarios_machine_learning & usuarios_data_science)  # usuarios q se repetem em ambas as listas

fez_ml_apenas = usuarios_machine_learning - usuarios_data_science  # usuarios q n se repetem em data science
print(15 in fez_ml_apenas)

print(usuarios_machine_learning ^ usuarios_data_science)  # fez um curso ou outro

#####
usuarios = {1, 5, 76, 34, 52, 13, 17}
usuarios.add(67216)  # é o append: adiciona o elemento ao conjunto, sem indexação
print(len(usuarios))
print(usuarios)

usuarios = frozenset(usuarios)  # congela um conjunto: não dá mais para add elementos
print(type(usuarios))

