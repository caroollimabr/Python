# https://docs.python.org/3/library/collections.html#collections.defaultdict
from collections import defaultdict

meu_texto = "O Fulano de Tal é um cavalheiro distinto".lower()
print(meu_texto)

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1  # COUNTER: verificar cada palavra
#    ate_agora = aparicoes[palavra]
#    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

# outra opção
dicionario = defaultdict(int)
dicionario['fulano'] = 15
dicionario['beltrano'] = 1
print(dicionario)
