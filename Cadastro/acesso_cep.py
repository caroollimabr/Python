import requests  # https://pypi.org/project/requests/, https://requests.readthedocs.io/en/master/


class BuscaEndereco:
    def __init__(self, cep):
        if self.cep_e_valido(str(cep)):
            self.cep = str(cep)
        else:
            raise ValueError("CEP inválido.")

    def __str__(self):
        return self.format_cep()

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:4], self.cep[5:])

    @property
    def acessa_via_cep(self):
        url = "http://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
