import time #importa a biblioteca
from random import randint #importa biblioteca
print('-='*20)
print("o computador escolheu um numero de 0 a 5")#mostra mensagem
print('-='*20)
print("processando...")
time.sleep(3)#coloca o computador em espera por 3 segundo
na = randint(0, 5) #faz o computador pensar no numero
nc = int(input("qual numero voçê acha que o computador escolheu?"))#o jogador tenta adivinhar
#print(na)
if nc==na:
    print("você acertou!!! o numero escolhido foi {}".format(na))
else:
    print("voçê errou! Tente novamente.\nO numero escolhido foi {}".format(na))