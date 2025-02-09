#calcula o fatorial de um numero e mostra na tela
from math import factorial
def fatorial(num, show = False):
    """
    -> calcula o fatorial de um numero
    :para 'num'; o valor a ser calculado
    :para 'show'; parementro opcinal (True ou False)
    :return; função sem retorno
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    if show:
        for c in range(num, 0, -1):
            print(f"{c}", end=' ')
            if c !=1:
                print("x ", end='')
        print('= ', end='')
    print(fat)


fatorial(4, True)
help(fatorial)#comando que descreve a função