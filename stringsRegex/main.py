from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"
argumentos_url = ExtratorArgumentosUrl(url)
moeda_origem, moeda_destino = argumentos_url.extrai_argumentos()
valor = argumentos_url.extrai_valor()
print(moeda_origem, moeda_destino, valor)

# Extrator_Argumentos_Url.url_valida("a")
# url = "moedaorigem=real&moedadestino=dolar"
# index = url.find("moedadestino") + len("moedadestino") + 1
# substring = url[index:]
# print(substring)

# string_velha = "bytebytebank"
# string_nova = string_velha.replace("byte", "carol", 1)  # procura o pedaço da string referenciada e troca 1 vez por "carol" (numa nova variável)
# print(string_nova)

# banco1 = "bytebank"
# banco2 = "Bytebank".lower()
# print(banco1 == banco2)  # python entende diferença entre maiúsculos e minúsculos

url_bytebank = "https://bytebank.com"
url1 = "https://buscasites.com/busca?q=https://bytebank.com"
url2 = "https://bitebank.com.br"
url3 = "https://bytebank.com/cambio/teste/teste"

# print(url2.find(url_bytebank))  # não encontrou
# print(url3.startswith(url_bytebank))
