import random

print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")

#random cria um número float aleatório. Round arredonda esse numero. Randrange(numero entre 1 e 100). Se colocar só random.randrange(100), o número aleatório será entre 0 e 99.
numero_secreto = round(random.randrange(1, 101))
print (numero_secreto)
total_de_tentativas = 3
# rodada é o nosso contador i
rodada = 1

while(rodada <= total_de_tentativas):
    #string interpolation no python "...{}".format(variavel)
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # input permite que o usuário digite algo (do tipo string)
    chute_str = input("Digite o seu número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    # transformando string em int
    chute = int(chute_str)

    if(chute < 1 and chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        # continue é o oposto do break
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    # no python, precisa ter 4 espaços abaixo do if
    # nos parênteses dos condicionais, há sempre bool
    # é possível usar parênteses ou não
    if acertou:
        print("Você acertou o número secreto!")
        # break finaliza o laço
        break
    else:
        if(maior):
            print("Seu número foi maior que o número secreto :(")
    #elif - else if
        elif(menor):
            print("Seu número foi menor que o número secreto :(")

    rodada = rodada + 1


print("FIM DO JOGO")
