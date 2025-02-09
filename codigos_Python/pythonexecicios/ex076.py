mercado = ('farinha', 4.5,
           'feijão', 10,
           'café', 4,
           'macarrão', 3,
           'miojo', 1.99,
           'refrigerante coca cola', 8.75,
           'açucar', 2.60)
print('-'*25)
print('preços dos produtos')
print('-'*25)
for item in range(0, len(mercado)):
    if item % 2 == 0:
        print(f'{mercado[item]:.<30} ', end='') #coloca no nome
    else:
        print(f'R${mercado[item]:>6.2f}') #coloca o preço