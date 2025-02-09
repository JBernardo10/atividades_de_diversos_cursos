nume = int(input("digite um numero: "))
cont = fatorial = nume

while cont != 0:
    print("{}".format(cont), end=' ')
    print(" x " if cont>1 else '=', end=' ')
    cont-=1
    if cont !=0:
        fatorial= fatorial*cont

print(fatorial)
print("\no fatorial de {} e {} ".format(nume, fatorial))
print("saiu")