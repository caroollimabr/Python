class ContaCorrente:
  def __init__ (self, numero_conta):
    self.numero_conta = numero_conta
    self.saldo = 0

  def deposita(self, valor):
    self.saldo += valor

  def __str__(self):
    return "[>>Número da conta: {} Saldo: {}<<]".format(self.numero_conta, self.saldo)


conta_carol = ContaCorrente(15456)
print(conta_carol)
conta_carol.deposita(50000)
print(conta_carol)
conta_fulano = ContaCorrente(54357)
print(conta_fulano)
conta_fulano.deposita(1000)
print(conta_fulano)

contas = [conta_carol, conta_fulano]
for conta in contas:
  print(conta)

contas = [conta_carol, conta_fulano, conta_carol]  # casa 2 referencia a casa 0
print(contas[0])

conta_carol.deposita(100)
print(contas[0])
print(contas[2])


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


contas = [conta_carol, conta_fulano]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

# contas.insert(0, 76051)  # adiciona um número inteiro à lista, e não outra conta (tipo diferente)
# print(contas[0], contas[1], contas[2])

# LISTAS SÃO MUTÁVEIS
# TUPLAS TÊM VALORES IMUTÁVEIS

# Se eu quiser mudar os valores, devo mudar o objeto:

conta_carol = (81723, 9000)
conta_fulano = (72881, 3000)


def deposita(conta):  # variação funcional (separo o comportamento dos dados)
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return codigo, novo_saldo


conta_carol = deposita(conta_carol)
print(conta_carol)

# Por mais que a tupla não possa ser modificada, o objeto presente nela pode:

conta_fulano = ContaCorrente(21340)
conta_fulano.deposita(500)
conta_carol = ContaCorrente(54049)
conta_carol.deposita(1000)
contas = (conta_carol, conta_fulano)

for conta in contas:
    print(conta)

contas[0].deposita(300)  # o obj será modificado
print(contas[0])
