# Em Python, cada caractere de uma string faz parte de um índice, como uma lista
meu_nome = "Carol"
sub_string = meu_nome[0:2]  # primeira (incluída) : última (não incluída)
print(sub_string)
outra_sub_string = meu_nome[:2]  # vá até índice 2
print(outra_sub_string)
minha_idade = 30
sobre_mim = "Meu nome é Carol e tenho 30 anos."
sub_string_frase = sobre_mim[11:]  # inicie a partir desse índice
print(sub_string_frase)

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
argumento = "moedaorigem=real"
index = argumento.find("=")
sub_string_argumento = argumento[index + 1:]  # para não incluir "="
print(sub_string_argumento)

# como encontrar o index certo em uma string grande
url_index = url.find("dolar")
print(url_index)

lista_argumento = argumento.split("=")  # separará os argumentos numa lista
print(lista_argumento)

string_nao_vazia = ""

if string_nao_vazia:  # se a string não estiver vazia
    print("Tem algo aqui")
else:
    print("Não tem nada aqui")