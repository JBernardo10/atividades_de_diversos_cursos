from datetime import date#importa uma funcao da biblioteca
atual = date.today().year#calcula o ano atual
nasc = int(input("ano de nascimento: "))#pede um dado
idade = atual - nasc#calcula a idade
print("quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))#mostra
if idade == 18:#compara se ja chegou na idade
    print("você tem que se alistar imediatamente")
elif idade < 18:#compara se é menor de idade
    saldo = 18 - idade
    print("você ainda não tem 18 anos. Faltam {} anos para o alistamento".format(saldo))
elif idade > 18:#compara se ja passou da idade
    saldo = idade - 18
    print("você já deveria ter se alistado a {} anos".format(saldo))
