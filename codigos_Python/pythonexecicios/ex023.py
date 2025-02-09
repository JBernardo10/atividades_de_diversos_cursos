#separa a um numero em suas casa
num = int(input('digite um numero:'))#pede um dado
#print("unidade: {}".)
#print("dezena: {}".format(num[2]))
#print("centena: {}".format(num[1]))
#print("milhar: {}".format(num[0]))
#n = str(num)
#print("analisando o numero {}".format(num))
#print('  a unidade: {}'
   #   '\n a dezena: {}'
  #    '\n a centena: {}'
 #     '\n o milhar: {}'
#      .format(n[3], n[2], n[1], n[0]))
uni = num // 1 % 10#calcula o resto da divisão inteira por 1
dez = num // 10 % 10#calcula o resto da divisão inteira por 10
cen = num // 100 % 10#calcula o resto da divisão inteira por 100
umi = num // 1000 % 10#calcula o resto da divisão inteira por 1000
print("Analisando o numero {}".format(num))#mostra os valores
print("A unidade: {}".format(uni))
print("A dezena: {}".format(dez))
print("A centena: {}".format(cen))
print("O milhar: {}".format(umi))