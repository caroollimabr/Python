from collections import Counter

texto1 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, 
totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 
Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, 
sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 
Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, 
sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. 
Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, 
nisi ut aliquid ex ea commodi consequatur? 
Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, 
vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
"""

texto2 = """
Pensando mais a longo prazo, 
a revolução dos costumes auxilia a preparação e a composição do sistema de participação geral.
Não obstante, a revolução dos costumes afeta positivamente a correta previsão do impacto na agilidade decisória.
O novo modelo estrutural aqui preconizado obstaculiza a apreciação da importância dos relacionamentos verticais 
entre as hierarquias.
A consolidação das estruturas prepara-nos para enfrentar situações atípicas decorrentes 
da gestão inovadora da qual fazemos parte.
É importante questionar o quanto o comprometimento entre as equipes apresenta tendências 
no sentido de aprovar a manutenção do processo de comunicação como um todo.
É importante questionar o quanto a revolução dos costumes nos obriga
à análise da gestão inovadora da qual fazemos parte.
Desta maneira, a expansão dos mercados mundiais causa impacto indireto 
na reavaliação da gestão inovadora da qual fazemos parte.
A prática cotidiana prova que a execução dos pontos do programa 
garante a contribuição de um grupo importante na determinação das diretrizes de desenvolvimento para o futuro.
"""


def analisa_frequencia_letras(texto):
    aparicoes = Counter(texto.lower())
    total_caracteres = sum(aparicoes.values()) # pegue todos os valores e somem eles para pegar o total de caracteres
    proporcoes = [(letra, frequencia / total_caracteres) for letra, frequencia in aparicoes.items()]  # pegue a porcentagem de aparições da letra
    proporcoes = Counter(dict(proporcoes))  # transforma a lista em um dicionário com contador
    mais_comuns = proporcoes.most_common(10)  # pega os resultados mais comuns

    for caractere, proporcao in mais_comuns:
        print("{} - {:.2f}%".format(caractere, proporcao * 100))


analisa_frequencia_letras(texto1)
analisa_frequencia_letras(texto2)
