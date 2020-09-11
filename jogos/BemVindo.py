import nome
import adivinhacaoFor
import forca

def bem_vindo():

    usuario = input("Digite seu nome: ")

    if(usuario):
        print("*********************************")
        print("Bem-vindo ao Carol jogos,", usuario, "!")
        print("*********************************")
    else:
        print("Usuário não identificado. Bem-vindo ao Carol jogos!")

    print("Lista de jogos")
    print("(1)Nome (2)Adivinhação (3)Forca")
    jogo = int(input("Escolha o seu jogo: "))

    if (jogo == 1):
        print("Iniciando o jogo dos nomes...")
        nome.jogar()
    elif jogo == 2:
        print("Iniciando o jogo da adivinhação...")
        adivinhacaoFor.jogar()

    if (jogo == 3):
        print("Iniciando o jogo da forca...")
        forca.jogar()

if(__name__ == "__main__"):
    bem_vindo()


