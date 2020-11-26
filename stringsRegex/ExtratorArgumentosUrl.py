class Extrator_Argumentos_Url:
    def __init__(self, url):
        if self.url_valida(url):
            self.url = url
        else:
            raise LookupError("URL inválida.")  # se url estiver vazia, retorne o seguinte erro com a msg

    @staticmethod
    def url_valida(url):
        if url:  # se a url não estiver vazia
            return True
        else:
            return False

    def extrai_argumentos(self):

        busca_moeda_origem = "moedaorigem"
        busca_moeda_destino = "moedadestino"

        # indice_inicial_moeda_destino = self.url.find("=", 15) + 1  # 15 é o índice
        # indice_inicial_moeda_origem = self.url.find("=") + 1
        # indice_final_moeda_origem = self.url.find("&")

        indice_inicial_moeda_destino = self.encontra_indice_inicial(busca_moeda_destino)
        indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find("&")

        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]
        moeda_destino = self.url[indice_inicial_moeda_destino:]

        return moeda_origem, moeda_destino

    def encontra_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada) + 1

