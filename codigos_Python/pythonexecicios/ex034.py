sa = float(input("Qual o valor de seu salário?"))#pede um dado
if sa<1250:#compara
    sal = sa + (sa*15/100)#faz calculo de porcentagem
    print("com o acrescimo de 15% seu salario agora é R${}".format(sal))
else:
    sal = sa + (sa*10/100)#faz calculo de porcentagem
    print("o seu salario agora é R${}".format(sal))
