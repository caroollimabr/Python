import re  # regex operations

frase1 = "Meu número é 1234-1234"
frase2 = "Fale comigo em 1234-1234, esse é o meu telefone"
frase3 = "1234-1234 é o meu celular"
frase4 = "dqwjn77775555ijdwqp8988-4567vhgjhkjwdk89218-9999lwkjbsqxuw91289-8888"

# padrao = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"
# padrao = "[0-9]{4}[-][0-9]{4}"  # pega o telefone no estilo 1111-1111
# padrao = "[0-9]{4,5}[-][0-9]{4}"  # pega o telefone no estilo 1111-1111 ou 11111-1111
padrao = "[0-9]{4,5}[-]*[0-9]{4}"  # retorna telefones COM OU SEM HÍFEN no estilo 1111-1111 ou 11111-1111

# retorno = re.search(padrao, frase4)  # procura padrão
# print(retorno.group())  # retorna tupla

retorno = re.findall(padrao, frase4)  # procura padrão
print(retorno)
