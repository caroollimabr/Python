# LISTAS SÃO MUTÁVEIS
# TUPLAS TÊM VALORES IMUTÁVEIS
fulano = ('Fulano', 32, 1988)
sicrano = ('Sicrano', 20, 2000)
# beltrano = (41, 'Beltrano', 1979) - valores semelhantes têm que ter a msm posição
usuarios = [fulano, sicrano]

usuarios.append(('Beltrano', 41, 1979))
print(usuarios)

usuarios[0][0] = ''