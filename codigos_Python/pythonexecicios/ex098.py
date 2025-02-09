from time import sleep


def lin():
    print("-="*20)


def contagem(inicio, fim, velocidade):
    if velocidade < 0:
        velocidade = velocidade * -1
    if velocidade == 0:
        velocidade = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += velocidade
            sleep(0.5)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= velocidade
            sleep(0.5)
    print("fim...")


lin()
print("contagem de 0 ate 10, ao passo de 1 em 1:")
contagem(0, 10, 1)
lin()
print("contagem de 10 ate 0, ao passo de 2 em 2:")
contagem(10, 0, -2)
lin()
print("personalize sua contagem:")
inicio = int(input("incio: "))
fim = int(input("fim: "))
passo = int(input("passo: "))
lin()
print(f"contegem personalizada, inicio {inicio} fim {fim}, ao passo {passo}")
contagem(inicio, fim, passo)