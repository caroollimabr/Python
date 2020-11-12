from abc import ABCMeta, abstractmethod  # abc: abstract classes


class Conta(metaclass=ABCMeta):  # classe Conta virou classe abstrata
  def __init__ (self, numero_conta):
    self.numero_conta = numero_conta
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  @abstractmethod  # sendo assim, vc força as classes filhas a criar essa classe
  def passa_o_mes(self):
    pass

  def __str__(self):
    return "[>>Número da conta: {} Saldo: {}<<]".format(self.numero_conta, self._saldo)


class ContaCorrente(Conta):
  def passa_o_mes(self):
      self._saldo -= 2


class ContaPoupanca (Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01  # somar 1%
        self._saldo -=3  # tira 3 reais


class ContaInvestimento(Conta):
    pass


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(100)
conta17.passa_o_mes()
print(conta17)

contas = [conta16, conta17]
for conta in contas:
    conta.passa_o_mes()  # duck typing - se responde a passa_o_mes(), faça passa_o_mes()
    print(conta)

# tupla: cada posição tem um significado diferente
# lista: elementos são tratados da mesma maneira




