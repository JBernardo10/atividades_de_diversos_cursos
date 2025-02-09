from datetime import date#importa uma função da biblioteca
ataul = date.today().year#pega o ano atual
nas = int(input("qual seu ano de nacmento? "))#pede um  dado
idade = ataul - nas#calcula a idade
print("O atleta tem {} anos".format(idade))#mostra
if idade <= 9:
    print("classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("classificação: JUNIOR")
elif idade <= 25:
    print("Classificação: SENIOR")
elif idade > 25:
    print("classificação: MASTER")
#compara as categorias