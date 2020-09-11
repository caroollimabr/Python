
def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de forca!")
    print("*********************************")

    palavra_secreta = "fulano"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    # False e True são valores, portanto estão em letra maiúscula

    while(not enforcou and not acertou):
        chute = input("Qual será a próxima letra? ")
        #strip() retira os espaços antes e depois da palavra, caso eles existam
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            #transformo as variáveis em string maiúsculas e comparo o chute com as letras da palavra secreta
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        #Aqui vai substituir os underscores
        print(letras_acertadas)

    print("FIM DE JOGO")

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
