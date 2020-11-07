#toma como entrada duas str: um arquivo e uma string
#exibe cada linha do arquivo que contém a string alvo como uma substring

def meuGrep(arquivo, alvo):
    arquivo_entrada = open(arquivo)
    for linha in arquivo_entrada:
        if alvo in linha:
            print(linha, end='')

print(meuGrep('arquivo.txt', 'ipsum'))