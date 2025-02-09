lista = []
while True:
    num = int(input('digite um valor: '))

    if num not in lista:
        lista.append(num)
        print('valor adicionado com suscesso.')
    else:
        print('valor ja exite na lista.')
    if 'n' == str(input('deseja continuar s/n: ')).lower():
        break
lista.sort()
print('voce digitou os seguintes valores: {}'.format(lista))