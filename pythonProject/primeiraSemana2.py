def palavras(): #aceita um arquivo de entrada e retorna a lista de palavras sem pontuação
    nome_arquivo = 'arquivo.txt'
    arquivo_entrada = open(nome_arquivo, 'r')
    conteudo = arquivo_entrada.read()
    arquivo_entrada.close()
    tabela = str.maketrans('!,.:;?', 6*' ')
    conteudo = conteudo.translate(tabela) #remove a pontuação pela string vazia
    conteudo = conteudo.lower()
    return conteudo.split()

print (palavras())
