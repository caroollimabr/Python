print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
# rodada é o nosso contador i
rodada = 1

# for variavel in range (inicial, final):
# se o contador tiver que ir de 3 em 3, por exemplo, é preciso adicionar um step nos parênteses:
# for rodada in range (1, total_de_tentativas+1, 3)
for rodada in range(1, total_de_tentativas+1):
    #string interpolation no python "...{}".format(variavel).
    # Posso formatar {:.2f} (f de float, 1.00, por exemplo) ou {:4.2f} ou {:04.2f} (ex. 0001.00)
    # Data {:02d}/{:02d} - numero inteiro ex. 04/09 (precisa colocar 0)
    # {nome.lower()}: transforma nome é lower case
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # input permite que o usuário digite algo (do tipo string)
    chute_str = input("Digite o seu número: ")
    print("Você digitou ", chute_str)
    # transformando string em int
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        # continue é o oposto do break (continue a interação). Ele pode servir para pular uma iteração if (i == 5): continue
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
