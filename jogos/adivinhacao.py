print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

# input permite que o usuário digite algo (do tipo string)
chute_str = input("Digite o seu número: ")

print("Você digitou ", chute_str)

#transformando string em int
chute = int(chute_str)

# no python, precisa ter 4 espaços
if numero_secreto == chute:
    print("Você acertou o número secreto!")
else:
    print("Você errou o número secreto :(")

print("FIM DO JOGO")
