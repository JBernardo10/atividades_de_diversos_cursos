def metade(n):
    return n/2


def dobro(n):
    return n*2


def aumentar(n, v):
    v = v / 100
    n = (n * v) + n
    return n


def diminuir(n, v):
    v = (100 - v) / 100
    n = n * v
    return n
