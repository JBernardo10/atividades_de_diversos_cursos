from random import randint
from time import sleep
#importa duas bibliotecas
itens = ('pedra', 'papel', 'tesoura')#cria uma tupla
computador = randint(0, 2)#randomiza um numero pseudo-aleatorio
print("suas opções são\n"
      "[ 0 ] pedra\n"
      "[ 1 ] papel\n"
      "[ 2 ] tesoura\n")#mostra as opcoes
jogador = int(input("qual será sua escolha? "))#pede uma escolha
print("jo")
sleep(1)
print("ken")
sleep(1)
print("po")
sleep(1)
#mostra mensagem com intervalos de tempo
print('-='*15)
print("o computador jogou {}".format(itens[computador]))
print("o jogador escolheu {}".format(itens[jogador]))
print('-='*15)
#mostra uma mensagem
if computador == 0: #jogou pedra. testa a primeira escolha do computador
      if jogador == 0:#testa o empate
            print("empate")
      elif jogador == 1:#testa a vitoria
            print("jogador venceu")
      elif jogador == 2:#testa a derrota
            print("computador venceu")

      else: print("jogada invalida")
elif computador == 1: #jogou papel
      if jogador == 0:
            print("computador venceu")
      elif jogador == 1:
            print("empate")
      elif jogador == 2:
            print("jogador venceu")

      else: print("jogada invalida")
elif computador == 2: #jogou tesoura
      if jogador == 0:
            print("jogador venceu")
      elif jogador == 1:
            print("computador venceu")
      elif jogador == 2:
            print("empatou")
      else: print("jogada invalida")