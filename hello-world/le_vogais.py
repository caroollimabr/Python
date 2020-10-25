def vogais(str):
    for i in range(len(str)):
        if str[i] in 'aeiouAEIOU':
            print(str[i])
vogais('Hortifrutigranjeiro')


def imprime_vogais():
    palavra = input("Digite uma palavra: ")
    for vogais in range(len(palavra)):
        if palavra[vogais] in 'aeiouAEIOU':
            print(palavra[vogais])

imprime_vogais()