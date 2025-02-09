import math as m #importando a biblioteca
cp = float(input('digite a medida do cateto oposto do triangulo:'))#pede um valor
ca = float(input('digite a medida do cateto adjecente do triangulo:'))#outro valor
#hi = (cp ** 2 + ca ** 2) ** (1/2)
hi = m.hypot(cp, ca)#com uma das funcções da bibiloteca calcula a hipotenusia
print(" a hypotenusa do seu triangulo correspode a:{:.2f} aproximadamente".format(hi))
