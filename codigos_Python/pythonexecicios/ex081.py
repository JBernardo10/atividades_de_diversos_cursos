lista = []
while True:
    lista.append(int(input('digite uma valor: ')))
    print('valor adicionado com suscesso.')
    if 'n' == str(input('deseja continuar s/n: ')).lower():
        break
lista.sort(reverse=True)
print(f'temos {len(lista)} valores na lista.\n')
print(f'A lista completa é {lista}\n')
if 5 in lista:
    print('o valor 5 está na lista.')
else:
    print('o valor 5 não está na lista.')