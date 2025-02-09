'''from random import randint
from time import sleep
#from operator import itemgetter
jogadores = {'jogado1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogadore3': randint(1, 6),
             'jogador4': randint(1,6)}
#ranking = dict()
for k, v in jogadores.items():
    print(f'O jogador {k} tem o valor {v}')
    sleep(1.5)
print("Ranking dos jogadores:")
#ranking = sorted(jogadores.items(), key= itemgetter(1), reverse = True)
cont =1
for d in sorted(jogadores, key = jogadores.get, reverse= True):
    print(f"{cont}º lugar: {d} com {jogadores[d]}:")
    cont+=1
    sleep(1.5)'''
'''
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar com {v[1]}.')
    sleep(1)
'''
from random import randint
from time import sleep
from operator import itemgetter
jogadas = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
print("valores sorteados:")
for k, v in jogadas.items():
    print(f"O {k} tirou: {v}")
    sleep(1.5)
raking ={}
raquink = sorted(jogadas.items(), key=itemgetter(1), reverse= True)
#coloca o dicinario em ordem em outro dicionario
print("posições:")
for k, v in enumerate(raquink):
    print(f"{k+1}º lugar {v[0]} tirou: {v[1]}")
    sleep(1.5)