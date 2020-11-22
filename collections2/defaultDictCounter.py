from collections import Counter

meu_texto = "O Fulano de Tal é um cavalheiro distinto".lower()
print(meu_texto)

aparicoes = Counter(meu_texto.split())  # https://docs.python.org/3/library/collections.html#collections.Counter
print(aparicoes)
