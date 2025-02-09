print("todo os numeros primos entre 1 e 500 são: ")
soma = 0
count = 0
for p in range(1, 501, 2):
    if p % 3 ==0:
        count += 1
        soma += p
print("a soma de todos os valores solicitados é{}".format(soma))
print("todos os valores colicitados {}".format(count))