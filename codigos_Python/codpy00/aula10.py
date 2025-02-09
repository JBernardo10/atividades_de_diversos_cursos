#tempo = int(input("quantos ano tem seu carro?"))
#if tempo<=5:
  #  print("seu carro ainda é novo!")
#else:
 #   print(" seu carro ja  está velho!")
#print("seu carro ainda está novo"if tempo<=5 else"seu carro ja está velho")
n1 = float(input("digite a primeira nota:"))
n2 = float(input("digite a segunda nota:"))
m = (n1 + n2)/2
print("a sua nota foi {:.1f}".format(m))
if m > 6.0:
    print("A sua media fo boa! PARABÉNS!")
else:
    print("sua media foi ruim! ESTUDE MAIS!")
print("-----fim------")
