from acesso_cep import BuscaEndereco
from datetime import datetime, timedelta # operações com tempo: https://docs.python.org/3/library/datetime.html#timedelta-objects
import re
import requests

# exercicio email
email_um = "fulano@gmail.com"
email_dois = "beltrano1993@4shared.org.uk"
email_tres = "sicrano@detal.br"
email_quatro = "fulaninho123@python.py.br"

def valida_email(email):
    padrao = "\w{2,50}@\w{2,15}\.[a-z]{2,3}\.?([a-z]{2,3})?"
    resposta = re.findall(padrao, email)

    if resposta:
        return True
    else:
        return False

print(valida_email(email_quatro))

# exercicio data

hoje = datetime.today()
hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M")
amanha = datetime.today() + timedelta(days=1, hours=20)
print(hoje)
print(amanha - hoje)
print(hoje_formatado)
print(type(hoje))
print(dir(datetime))  #verificar possibilidades de métodos

# hora
agora = datetime.now()
agora_formatado = agora.strftime("%Y/%m/%d-%H:%M:%S")
print(agora_formatado)

# usando biblioteca requests para realizar requisições
req = requests.get("http://viacep.com.br/ws/01001000/json/")
print(req.text)
print(type(req.text))

# cep
cep = "01000000"
obj_cep = BuscaEndereco(cep)
acesso = obj_cep.acessa_via_cep()
print(type(acesso.text))
print(type(acesso.json()))  # melhor usar tipo dicionario
print(acesso.json())
print(acesso.json()['cep'])
print(acesso.json()['bairro'])
bairro, cidade, uf = obj_cep.acessa_via_cep
print(bairro, cidade, uf)
