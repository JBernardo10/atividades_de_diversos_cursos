from datetime import date#importando uma função da biblioteca
ano = int(input("que nao quero analisar? \ncoloque 0 para analisar o ano atual::"))#mostrando na tela
if ano == 0:#comparando
    ano = date.today().year#salvando o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:#comparando se o ano é bissexto
    print("o ano {} é bissexto".format(ano))
else:
    print("o ano {} não é bissexto".format(ano))
