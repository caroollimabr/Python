from collections import defaultdict

class Conta:
    def __init__(self):
        print("Criando uma conta")


contas = defaultdict(Conta)
contas[12390]
contas[82678]
print(contas)
