#package em Python chama-se module
class Conta: #uma classe deve ter uma única responsabilidade (aqui não é para ter método "é inadimplente", por ex.
    def __init__(self, numero, titular, saldo, limite): #método/função construtor. Self é a referência/endereço do objeto
        print("Construindo objeto {}".format(self))
        self.__numero = numero # . significa "acesse" #__ indica private: pode ser usado apenas dentro da classe, ou seja, o atributo recebe o nome da classe como prefixo
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def tira_extrato (self):
        print("Saldo de {} da(o) titular {}".format(self.__saldo, self.__titular))

    def deposita (self, valor):
        self.__saldo += valor

    def saca (self, valor):
        self.__saldo -= valor

    def transfere (self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #garbage collector: o python procura objetos que não são utilizados e jogam eles no lixo
    #se quisermos desfazer uma referência,pode-se usar None: >>> outraRef = None

#S - Single responsibility principle
#O - Open/closed principle
#L - Liskov substitution principle
#I - Interface segregation principle
#D - Dependency inversion principle