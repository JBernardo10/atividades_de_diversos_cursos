from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=' * 15)
print("joga na mega sena")
print('-=' * 15)
quant = int(input("quantos jogos voçe quer que eu sorteie? "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont+= 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-='*3, '< boa sorte >', '-='*3)
