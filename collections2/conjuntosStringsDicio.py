meu_texto = "O Fulano de Tal é um cavalheiro distinto"
print (set(meu_texto.split(" ")))  # split transforma o texto em um conjunto de palavras

# DICIONÁRIO: mapear chaves com valores
aparicoes = {
    "Verbos": 1,
    "Artigos": 2,
    "Adjetivos": 1,
    "Substantivos comuns": 1
}

print(type(aparicoes))
print(aparicoes["Artigos"])

outra_forma_dicio = dict (Verbos = 1, Artigos = 2)
print(outra_forma_dicio)

# OPERAÇÕES
aparicoes["Verbos"] = 80  # modifica valor
print(aparicoes)
del aparicoes["Substantivos comuns"]  # deleta elemento
print(aparicoes)
print("Substantivos comuns" in aparicoes)  # procura elemento dentro do conjunto/lista/dict/etc

for classe in aparicoes:  # iterar chaves
    print(classe)

for classe in aparicoes.keys():   # iterar chaves
    print(classe)

for classe in aparicoes.values():  # iterar valores
    print(classe)

print(1 in aparicoes.values())

for classe in aparicoes.keys():  # itera tudo
    print(classe, aparicoes[classe])

for classe, valor in aparicoes.items():  # itera tudo
    print(classe, "=", valor)

for classe in aparicoes.items():  # (itera tudo com tuplas '')
    print(classe)

print (["classe {}".format(classe) for classe in aparicoes.keys()])  # classe verbos, classe artigos, etc...

