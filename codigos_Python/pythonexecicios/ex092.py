'''import datetime
ano = datetime.date.today().year
pessoa = dict()
pessoa['nome'] = str(input("Digite seu nome: ")).strip().capitalize()
pessoa['idade'] = ano - int(input("Digite seu ano de nascimento: "))
pessoa['carteira'] = int(input("Carteira de trabalho (0 não possui): "))
if pessoa['carteira'] != 0:
    pessoa['contratação'] = int(input("Ano de acontração: "))
    pessoa['salario'] = float(input('Salario: R$ '))
    pessoa['aposentadoria'] = pessoa['contratação'] + 35
print("-="*25)
for k, v in pessoa.items():
    print(f"{k} tem o valor {v}")'''
import datetime
dados = dict()
dados['nome'] = str(input("informe seu nome: ")).strip().title()
ano = int(input("informe seu ano de nascimento: "))
dados['idade'] = datetime.date.today().year - ano
dados['ctps'] = int(input("informe sua carteirade trabalho, caso não "
                          "tenha digite [0]: "))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input("informe o ano de contratação: "))
    dados['salario'] = float(input("informe o salário: "))
    dados['aposentadoria'] = (dados['contratacao'] + 35)
for k, v in dados.items():
    print(f"o campo {k} contem o dado {v}")