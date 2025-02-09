n1 = float(input("digite o primeiro numero:"))#pede um dado
n2 = float(input("digite o segundo numero:"))#pede um dado
n3 = float(input("digite o terceiro numero:"))#pede um dado
#verificando o maior
if n1 > n2:
    a = n1
else: a = n2
if a > n3:
    print("o maior valor é {}".format(a))
else: print("o maior valor é {}".format(n3))
#verificando o menor
if n1 < n2:
    a = n1
else: a = n2
if a < n3:
    print("o menor valor é {}".format(a))
else: print("o menor valor é {}".format(n3))