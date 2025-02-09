def metade(n=0):
    return n/2


def dobro(n=0):
    return n*2


def aumentar(n=0, v=0):
    v = v / 100
    n = (n * v) + n
    return n


def diminuir(n=0, v=0):
    v = (100 - v) / 100
    n = n * v
    return n


def moeda(preco=0, moeda="R$"):
    return f"{moeda}{preco:<8.2f}".replace('.', ',')
