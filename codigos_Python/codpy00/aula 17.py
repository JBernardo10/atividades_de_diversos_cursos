'''num = [1, 2, 8, 9]
num[2] = 5
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2)
print(num)
print(f"essa lista tem {len(num)} elementos")
valores = list()
for cont in range(0, 5):
    valores.append(int(input("digite um valor: ")))

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}')
print("cheguei ao final.")'''

a = [2, 3, 4, 7]
b = a[:] #criando uma copia dos valores de a
#a = b igualando as lista, cria uma ligação entre elas
b[2] = 6
print(" lista a {}".format(a))
print(" lista b {}".format(b))