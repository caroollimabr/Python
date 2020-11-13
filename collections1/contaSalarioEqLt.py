from operator import attrgetter
from functools import total_ordering
from herancaPolimorfismo import ContaCorrente


@total_ordering  # agora dá para comparar >, <, ==, etc: https://docs.python.org/3/library/functools.html
class ContaSalario:
    def __init__(self, numero_conta):
        self._numero_conta = numero_conta
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Número da conta: {} Saldo: {}<<]".format(self._numero_conta, self._saldo)

    def __eq__(self, outra):  # método de verificação de igualdade
        if type(outra) != ContaSalario:
            return False

        return self._numero_conta == outra._numero_conta and self._saldo == outra._saldo

    def __lt__(self, outra):  # less than, método para comparar saldos
        if self._saldo != outra._saldo:
            return self._saldo < outra._saldo
        return self._numero_conta < outra._numero_conta  # se não, ordene pelo número da conta


conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

print(conta2 == conta1)  # esses dois objetos têm os mesmos valores, mas são distintos. É possível determinar que elas são iguais com o método __eq__

contas = [conta1]
print(conta1 in contas)
print(conta2 in contas)

conta1.deposita(100)  # agora não são mais iguais
print(conta1 == conta2)

conta3 = ContaSalario(37)
conta4 = ContaCorrente(37)
print(conta3 == conta4)  # não são iguais pq os tipos são diferentes

print(isinstance(ContaCorrente(37), ContaCorrente))  # pergunta se o obj é de determinado tipo

conta_fulano = ContaSalario(11)
conta_fulano.deposita(500)
conta_sicrano = ContaSalario(22)
conta_sicrano.deposita(200)
conta_beltrano = ContaSalario(33)
conta_beltrano.deposita(4000)

contas = [conta_fulano, conta_sicrano, conta_beltrano]

print (conta_fulano > conta_sicrano)

print (conta_fulano < conta_sicrano)

#  print(sorted(contas))  # não dá pq sorted usa menor para comparar itens. Não dá para comparar objs assim

for conta in sorted(contas):  # ordem crescente tendo em vista o saldo
    print(conta)

for conta in sorted(contas, reverse=True):  # ordem decrescente
    print(conta)


def extrai_saldo(conta):
    return conta._saldo


for conta in sorted(contas, key=extrai_saldo):  # para ordenar, preciso ter apenas um parâmetro de comparação, o saldo por ex
    print(conta)

# outra opção
for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

conta1 = ContaSalario(37)
conta1.deposita(500)

conta2 = ContaSalario(38)
conta2.deposita(500)

conta3 = ContaSalario(39)
conta3.deposita(499)

contasSalario = [conta1, conta2, conta3]

for conta in sorted(contasSalario):
    print(conta)

print(conta2 >= conta1)  # graças a @total_ordering