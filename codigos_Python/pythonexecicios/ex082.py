lista = list()
while True:
    lista.append(int(input('digite uma valor: ')))
    print('valor adicionado com suscesso.')
    if 'n' == str(input('deseja continuar s/n: ')).lower():
        break
listapar = list()
listaimpar = list()
for c in lista:
    if c %2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print(f'A lista completa é {lista}')
print(f'Os nuúmeros pares presentes na lista são{listapar}')
print(f'E os numeros impares presentes na lista são {listaimpar}')