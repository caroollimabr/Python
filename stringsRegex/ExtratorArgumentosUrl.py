class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.url_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("URL inválida.")  # se url estiver vazia, retorne o seguinte erro com a msg

    @staticmethod
    def url_valida(url):
        if url and url.startswith("https://bytebank.com"):  # se a url não estiver vazia
            return True
        else:
            return False

    def extrai_argumentos(self):

        busca_moeda_origem = "moedaorigem=".lower()
        busca_moeda_destino = "moedadestino=".lower()

        # indice_inicial_moeda_destino = self.url.find("=", 15) + 1  # 15 é o índice
        # indice_inicial_moeda_origem = self.url.find("=") + 1
        # indice_final_moeda_origem = self.url.find("&")

        indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find("&")
        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()
            indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
            indice_final_moeda_origem = self.url.find("&")
            moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        indice_inicial_moeda_destino = self.encontra_indice_inicial(busca_moeda_destino)
        indice_final_moeda_destino = self.url.find("&valor")
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]  # quando encontrar "moedadestino=", vai retornar o que vem dps dela

        return moeda_origem, moeda_destino

    def encontra_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino", "real", 1)  # troca a primeira ocorrencia de moedadestino por real
        print(self.url)

    def extrai_valor(self):
        busca_valor = "valor="
        indice_inicial_valor = self.encontra_indice_inicial(busca_valor)
        valor = self.url[indice_inicial_valor:]  # quando encontrar "valor=", vai retornar o que vem dps dela
        return valor
