#def soma(a, b):
 #   print(f"o valor de A = {a}, B = {b}")
  #  s = a + b
   # print(f"a soma de A + B = {s}")


#programa principal
#soma(b=4, a=6)
#soma(15, 25)
#soma(2, 1)
#def contador(*num):
 #   for valor in num:
  #      print(valor, end='')
   # print(' fim...')
    #print(len(num))


#contador(7, 1, 2, 9, 3)
#contador(1, 2, 9, 12)
#contador(1)

def dobra_valores(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [2, 6, 5, 10, 12]
dobra_valores(valores)
print(valores)

def soma(*num):
    soma = 0
    for valor in num:
        soma += valor
    print(f"a soma dos valores {num} é {soma}")


soma(2, 3, 6)
soma(5, 1, 6, 9, 9)