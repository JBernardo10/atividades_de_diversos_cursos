saida = 0
soma = valores = 0
saida = int(input("digite um numero, ou 999: "))
while saida != 999:
    valores+=1
    soma +=saida
    saida = int(input("digite outros numeros, ou 999:  "))
print("a soma dos valores digitados e {} e a quantidade de numeros digitados foram {}".format(valores, soma))