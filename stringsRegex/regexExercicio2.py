import re

frase1 = "podemos marcar de sair sabado 23h"
frase2 = "acho que quinta 21h é a melhor hora para a gente ir lá"
frase3 = "terca 19h é um bom momento para sairmos"

padrao = "[a-z]{1,20}[ ][0-9]{1,2}[h]"

retorno = re.findall(padrao, frase1)
retorno1 = re.findall(padrao, frase2)
retorno2 = re.findall(padrao, frase3)
print(retorno, retorno1, retorno2)
