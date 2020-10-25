def calcula_media(n1, n2, n3):
 media = (3 / ((1/(n1+4)) + (1/(n2+4)) + (1/(n3+4)))) - 4
 return media
n1 = input('Digite a nota 1: ')
n2 = input('Digite a nota 2: ')
n3 = input('Digite a nota 3: ')
n1 = eval(n1)
n2 = eval(n2)
n3 = eval(n3)
media = calcula_media(n1, n2, n3)
if media >= 5:
 print('Você passou, sua média é ', media)
else:
 print('Você não passou, sua média é ', media)
