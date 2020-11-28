import re

padrao = "e[0-9]{1,2} [s,t][0-9]{1,2}"
conversa1 = "Estou no e 1 t 3 de Friends"
conversa2 = "O e02 t2 é o melhor de How I Met Your Mother"
conversa3 = "Eu parei GOT no e2 s3"
conversa4 = "Não gostei do ep4 t5 de Vikings"
conversa5 = "O melhor episódio de Stranger Things é o e011 s02"

retorno = re.findall(padrao, conversa1)
retorno1 = re.findall(padrao, conversa2)
retorno2 = re.findall(padrao, conversa3)
retorno3 = re.findall(padrao, conversa4)
retorno4 = re.findall(padrao, conversa5)
print(retorno, retorno1, retorno2, retorno3, retorno4)