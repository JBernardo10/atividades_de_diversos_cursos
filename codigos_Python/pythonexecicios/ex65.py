entrada = 's'
cont = soma = 0
maior = menor = 0
while entrada == 's':
    valor = int(input("digite um valor: "))
    cont += 1
    soma += valor
    if cont == 1:
        menor = maior = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    entrada = str(input("quer continuar [S/N]: ")).lower()
print("a media dos valores digitados e {:.2f}, o maior valor e {} e o menor valor e {}".format(soma/cont, maior, menor))