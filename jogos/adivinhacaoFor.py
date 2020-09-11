# built-in functions vc não precisa importar, pois estão disponíveis para uso automaticamente
# and sequence types: https://docs.python.org/3/library/functions.html exs. type(), abs(), input(), int...
import random

#def define uma função (pode ter parametros tb. ex: def soma(a, b): return a + b)
def jogar():

    print("*********************************")
    print("Bem-vindo ao jogo de adivinhação!")
    print("*********************************")

    #random cria um número float aleatório. Round arredonda esse numero
    numero_secreto = round(random.random() * 100)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual é o nível de dificuldade?")
    print("(1)Fácil (2)Médio (3)Difícil")

    nivel = int(input("Defina o seu nível: "))

    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 1

    # rodada é o nosso contador i
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
            print("Você acertou o número secreto e fez {} pontos!".format(pontos))
            # break finaliza o laço
            break
        else:
            if(maior):
                print("Seu número foi maior que o número secreto :(")
        #elif - else if
            elif(menor):
                print("Seu número foi menor que o número secreto :(")
            #Absoluto - abs(calculo) - resposta do calculo sem sinal, para que no caso do numero ser menor que o chute, a pessoa não ganhe pontos
            pontos_perdidos = round(abs(numero_secreto - chute)/3) #ex. 10 - 20 = -20,  problema pq a pessoa ganharia pontos
            pontos = pontos - pontos_perdidos
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))


        rodada = rodada + 1


    print("FIM DO JOGO")

if(__name__ == "__main__"):
    jogar()

