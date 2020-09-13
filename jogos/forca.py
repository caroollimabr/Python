import random

def jogar():
    imprimir_mensagem_abertura()
    palavra_secreta = carregar_palavra_secreta()
    # LIST COMPREHENSIONS: coloca um "_" para cada letra da palavra
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    # False e True são valores, portanto estão em letra maiúscula
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pedir_chute()

        if(chute in palavra_secreta):
            marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Eita, a palavra não possui essa letra. Faltam {} tentativas.".format(7 - erros))
            desenhar_forca(erros)

        enforcou = erros == 7
        # Enquanto houver "_" em letras acertadas, eu ainda não acertei
        acertou = "_" not in letras_acertadas
        # Aqui vai substituir os underlines
        print(letras_acertadas)

    if(acertou):
        imprimir_mensagem_vencedor()
    else:
        imprimir_mensagem_game_over(palavra_secreta)
    print("FIM DE JOGO")

# Funções do jogo
def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def imprimir_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprimir_mensagem_game_over(palavra_secreta):
    print("Que pena, você foi enforcado :(")
    print("A palavra era {}.".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        # comparo o chute com as letras da palavra secreta
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1 # index = index + 1

def pedir_chute():
    chute = input("Qual será a próxima letra? ")
    # strip() retira os espaços antes e depois da palavra, caso eles existam
    chute = chute.strip().upper()
    return chute

def inicializar_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def imprimir_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carregar_palavra_secreta():
    arquivo = open("palavrasForca.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
# Poderia ser assim:
# def carrega_palavra_secreta(nome_arquivo="palavras.txt", primeira_linha_valida=0):
#     arquivo = open(nome_arquivo, "r")
#     palavras = []
#
#     ….
#
#     numero = random.randrange(primeira_linha_valida, len(palavras))
#     palavra_secreta = palavras[numero].upper()
#
#     return palavra_secreta

if(__name__ == "__main__"):
    jogar()







#chute = chute.strip()
#quando variavel.find("bla") não encontra nada, ele devolve -1. Caso encontre, vai devolver a posição do elemento em questão, começando do 0.
#palavra.capitalize() devolve 'Fulano'
#palavra.lower() devolve 'fulano'
#palavra.upper() devolve 'FULANO'
#palavra.endswith("o") devolve True
#https://docs.python.org/3/library/functions.html

#valores = [0,1,2,8]
#min(valores) devolve 0 - o elemento da primeira posição
#max(valores) devolve 8 - o elemento da última posição
#len(valores) devolve 5 - quantas posições a lista tem
#valores.append(7) - inclui o 7 a lista valores = [0,1,2,8,7]
#valores.count(7) - devolve 1, pois há apenas um valor 7 na lista
#valores.index(7) devolve 4, pois é a posição em que o valor 7 se encontra na lista. Caso não exista, ele emite um erro.

#serie = range(0,3) - cria uma lista serie = [0,1,2,3]
#serie.pop() apaga o último elemento - serie = [0,1,2]
#serie1 = tuple(serie) transforma serie em tuple: serie1 = (0,1,2)
#serie2 = list(serie1) transforma serie1 em tuple: serie2 = [0,1,2]

#TUPLE: LISTA COM PARÊNTESES QUE É IMUTÁVEL (NÃO É UM LIST [], range ou str QUE são MUTÁVEIS)
#estacoes = ("verao", "outono", "inverno", "primavera")

#SET: coleção MUTÁVEL QUE NÃO POSSUI ÍNDICE (não é ordenado), MAS não podem existir elementos duplicados
#cpfs = {11122233344, 22233344455, 33344455566}
#instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30} - DICTIONARY. As idades estão relacionadas aos nomes, quando eu pedir o nome, vai vir a idade

#SUMMING UP...
#Coleções em Python: 1 list[indice], 2 tuple(imutavel, indice), 3 str"indice", 4 range[list indice], 5 set{nao tem valor duplicado}

# LIST COMPREHENSIONS
# Ao invés de
# frutas = ["maçã", "banana", "laranja", "melancia"]
# lista = []
# for fruta in frutas:
#     lista.append(fruta.upper())

# USE AS LIST COMPREHENSIONS:
# lista = [fruta.upper() for fruta in frutas]

#inteiros = [1,3,4,5,7,8]
#quadrados = [n*n for n in inteiros]

#inteiros = [1,3,4,5,7,8,9]
# pares = []
# for numero in inteiros:
#     if numero % 2 == 0:
#         pares.append(numero)
# ----AO INVÉS DISSO, USANDO LIST COMPREHENSION:
# inteiros = [1,3,4,5,7,8,9]
# pares = [x for x in inteiros if x % 2 == 0]

# NO CONSOLE
# open ("arquivo.txt", "w") - w vem de write
# arquivo = open("arquivo.txt", "a") a vem de append
# arquivo = open("arquivo.txt", "r") a vem de read
# ler = arquivo.read() - Vê o que tem dentro
# ler_linha = arquivo.readline() - Vê apenas uma linha do arquivo (leitura de modo controlado)
# print(ler_linha)
# arquivo.write("fulano\n") - vc está escrevendo dentro do arquivo
# arquivo.close()

# imagem = open("foto.jpg", "rb")
# Por exemplo, o código abaixo cria uma cópia de uma imagem:
#
# #arquivo copia.py
# logo = open('python-logo.png', 'rb')
# data = logo.read() ---read() lê o arquivo inteiro de uma vez, colocando o ponteiro de leitura no final do mesmo. Se chamarmos a função read() novamente, nada será lido por causa disso.
# logo.close()
#
# logo2 = open('python-logo2.png', 'wb')
# logo2.write(data)
# logo2.close()

# sintaxe para abertura de arquivo:
# with open("palavras.txt") as arquivo:
#     for linha in arquivo:
#         print(linha)

# EVITE USAR VARIAVEIS GLOBAIS, O IDEAL É QUE ELA SEJA VISIVEL APENAS DENTRO DA FUNÇÃO
# PENSE NA VIABILIDADE DA FUNÇÃO: SE ELA RETORNA POUCA COISA, TALVEZ VALHA A PENA DEIXÁ-LA JUNTO AO CÓDIGO
# Funções são importantes também para dar melhor visibilidade, teste e manutenção do código