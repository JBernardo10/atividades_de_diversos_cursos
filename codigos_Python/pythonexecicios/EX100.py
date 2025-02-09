from random import randint
from time import sleep


def soteia():
    valores = list()
    print("sorteando os 5 valores na lista: ")
    for c in range(0, 5):
        valores.append(randint(0, 20))
        print(f'{valores[c]} ', end='')
        sleep(1)
    print("pronto...")
    somaPar(valores)


def somaPar(valores):
    resultado= 0
    for c in range(len(valores)):
        if valores[c] %2 == 0:
            resultado += valores[c]
    print(f'a soma dos valores par de {valores} é {resultado}')


soteia()