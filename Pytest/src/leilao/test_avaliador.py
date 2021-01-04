from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    # cenarios
    def setUp(self):  # metodo que cria cenários sem precisar invocá-lo em tds os testes
        self.sicrano = Usuario('Sicrano')
        self.lance_sicrano = Lance(self.sicrano, 1500.0)
        self.leilao = Leilao('Quadro')

    # padrões nomenclatura:
    # test_quando_adicionados_em_ordem_crescente_deve_retornar_maior_e_menor_valor_de_lance(self):
    def test_deve_retornar_maior_e_menor_valor_de_lance_quando_adicionados_em_ordem_crescente(self):
        fulano = Usuario('Fulano')
        lance_fulano = Lance(fulano, 1000.0)

        self.leilao.lances.append(lance_fulano)
        self.leilao.lances.append(self.lance_sicrano)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 1000.0
        maior_valor_esperado = 1500.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_maior_e_menor_valor_de_lance_quando_adicionados_em_ordem_decrescente(self):
        fulano = Usuario('Fulano')
        lance_fulano = Lance(fulano, 1000.0)

        self.leilao.lances.append(self.lance_sicrano)
        self.leilao.lances.append(lance_fulano)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 1000.0
        maior_valor_esperado = 1500.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_lance(self):
        self.leilao.lances.append(self.lance_sicrano)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(1500.0, avaliador.menor_lance)
        self.assertEqual(1500.0, avaliador.maior_lance)

    def test_deve_retornar_maior_e_menor_valor_quando_leilao_tiver_tres_lances(self):
        fulano = Usuario('Fulano')
        beltrano = Usuario('Beltrano')

        lance_fulano = Lance(fulano, 1000.0)
        lance_beltrano = Lance(beltrano, 2000.0)

        leilao = Leilao('Quadro')

        leilao.lances.append(self.lance_sicrano)
        leilao.lances.append(lance_fulano)
        leilao.lances.append(lance_beltrano)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 1000.0
        maior_valor_esperado = 2000.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)


