#package em Python chama-se module
class Conta:
    def __init__(self, numero, titular, saldo, limite): #método/função construtor. Self é a referência/endereço do objeto
        print("Construindo objeto {}".format(self))
        self.numero = numero # . significa "acesse"
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
