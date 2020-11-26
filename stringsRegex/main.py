from ExtratorArgumentosUrl import Extrator_Argumentos_Url

url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar"
argumentos_url = Extrator_Argumentos_Url(url)
moeda_origem, moeda_destino = argumentos_url.extrai_argumentos()
print(moeda_origem, moeda_destino)
Extrator_Argumentos_Url.url_valida("a")

# url = "moedaorigem=real&moedadestino=dolar"
# index = url.find("moedadestino") + len("moedadestino") + 1
# substring = url[index:]
# print(substring)