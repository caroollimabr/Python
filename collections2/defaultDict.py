# https://docs.python.org/3/library/collections.html#collections.defaultdict
from collections import defaultdict

meu_texto = "O Fulano de Tal é um cavalheiro distinto"
meu_texto = meu_texto.lower()
print(meu_texto)

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1  # verificar cada palavra

print(aparicoes)

####### outra opção
dicionario = defaultdict(int)
dicionario['fulano'] = 15
print(dicionario)