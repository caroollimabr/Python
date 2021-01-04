from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

fulano = Usuario('Fulano')
sicrano = Usuario('Sicrano')

lance_fulano = Lance(fulano, 1000.0)
lance_sicrano = Lance(sicrano, 1500.0)

leilao = Leilao('Quadro')

leilao.lances.append(lance_fulano)
leilao.lances.append(lance_sicrano)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}.')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance for de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')

