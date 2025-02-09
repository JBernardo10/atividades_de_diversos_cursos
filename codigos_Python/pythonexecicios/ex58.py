import time
from random import randint
print('-='*20)
print("o computador escolhera um numero de 0 a 10")
print('-='*20)
print("processando...")
time.sleep(3)
na = randint(0, 10) #faz o computador pensar no numero
palpite = 0
acertou = False
while not acertou:
    njoador = int(input("qual numero voçê acha que o computador escolheu?"))#o jogador tenta adivinhar
    palpite+= 1
    if njoador==na:
        print("você acertou!!! o numero escolhido foi {}, e qualtidade de palpites foram {}".format(na, palpite))
        acertou = True
    else:
        print("voçê errou! Tente novamente")
print("saiu")