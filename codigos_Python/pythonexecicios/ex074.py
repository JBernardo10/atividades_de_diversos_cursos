from random import randint
numeros = (randint(0, 15), randint(0, 15), randint(0, 15), randint(0, 15), randint(0, 15))
for n in numeros:
    print(f'{n}', end=', ')
print(f'\no maior valor sorteado foi {max(numeros)}')
print(f'o menor valor sorteado foi {min(numeros)}')