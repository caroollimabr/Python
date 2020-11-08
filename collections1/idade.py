# uso coleções quando eu quero trabalhar com diversos valores do mesmo tipo

idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

# muito trabalhoso
print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [39, 30, 27, 18]
type(idades)
len(idades)
idades[0]  # vc pode chamar assim no console python
idades.append(15)  # adiciona ao fim da lista
idades.append([12,13])  # adiciona uma lista ao fim da lista. Não dá pra por mais de uma idade ()
for elemento in idades:  #vejá que o último elemento adicionado é tipo lista, e não um inteiro como os outros
  print("Recebi o elemento", elemento)
for idade in idades:
  print(idade)
idades.remove(27) # remove a primeira vez que o elemento aparecer
idades.clear()  # remove toda a lista. Leia mais em https://docs.python.org/3/tutorial/datastructures.html
idades  # vc pode chamar assim no console python

idades = [11, 12, 27, 18]
28 in idades  # pergunta se 28 está na lista idades. Vc pode chamar assim no console python

if 12 in idades:
  idades.remove(12)

idades = [11, 12, 27, 18]
idades.insert(0, 20)  # adiciona a idade 20 na posição 0
idades.extend([28, 19])  # adiciona dois ou mais itens dentro da lista (ao final dela)

idades_no_ano_que_vem = []  # transformar os valores do array anterior em outro array com modificações
for idade in idades:
  idades_no_ano_que_vem.append(idade + 1)
print(idades_no_ano_que_vem)

idades_daqui_2_anos = [(idade + 2) for idade in idades]  # outra forma de transformar os valores do array anterior em outro array com modificações
print(idades_daqui_2_anos)

[idade for idade in idades if idade > 21]  # pegar todas as idades menores que 21

def proximo_ano(idade):
  return idade + 1
[proximo_ano(idade) for idade in idades if idade > 21]

def faz_processamento_visualizacao(lista):
  print(len(lista))

idades = [16, 21, 29, 56, 43]
faz_processamento_visualizacao(idades)  # lista mutável
print(idades)

def faz_processamento(lista = None):  # não coloco lista = [] pq toda vez que rodar o vazio vai ocupar um vazio na memória
  print (len(lista))