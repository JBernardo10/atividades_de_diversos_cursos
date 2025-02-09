from time import sleep


def maiorr(*numeros):
    print("analisando os valores passados...")
    maiorn = 0
    for c in numeros:
        print(f"{c}, ", end='')
        if maiorn == 0:
            maiorn = c
        elif c > maiorn:
            maiorn = c
        sleep(0.5)
    print(f'\nao todo foram passados {len(numeros)} valores.\nO maior valor é {maiorn}')


maiorr(1, 3, 6, 9, 12)
print("-="*10)
maiorr(-1, 4, 90, 5)
maiorr(6)
