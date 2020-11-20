# https://docs.python.org/3/library/stdtypes.html#str.lower
meu_texto = "O Fulano de Tal é um cavalheiro distinto e distinto ele é"
meu_texto = meu_texto.lower()
print(meu_texto)

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)  # GET verifica se palavra está no dicionário
    aparicoes[palavra] = ate_agora + 1  # verificar cada palavra

print(aparicoes)
