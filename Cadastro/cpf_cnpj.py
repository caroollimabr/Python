# https://pypi.org/project/validate-docbr/
# Factory method: https://sourcemaking.com/design_patterns/factory_method
# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod  # método estático para ser pai "factory"
    def cria_documento(documento):  # verifica que tipo de doc está recebendo
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta.")

class DocCpf:  # classes filhas têm métodos iguais
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido.")

    def __str__(self):  # para validar algo com length, precisa ser string, não pode ser inteiro
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    # mask() retorna  "{}.{}.{}-{}".format(doc[:3], doc[3:6], doc[6:9], doc[-2:])
    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError ("CNPJ inválido.")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    # mask() retorna  "{}.{}.{}/{}-{}".format(doc[:2], doc[2:5], doc[5:8], doc[8:12], doc[-2:])
    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cpf)

