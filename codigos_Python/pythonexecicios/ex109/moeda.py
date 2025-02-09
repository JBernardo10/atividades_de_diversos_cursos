def metade(n=0, form=False):
    res = n/2
    return res if form is False else moeda(res)


def dobro(n=0, form=False):
    res = n*2
    return res if form is False else moeda(res)


def aumentar(n=0, v=0, form=False):
    v = v / 100
    res = (n * v) + n
    return res if form is False else moeda(res)


def diminuir(n=0, v=0, form=False):
    v = (100 - v) / 100
    res = n * v
    return res if form is False else moeda(res)


def moeda(preco=0, moeda="R$"):
    return f"{moeda}{preco:<8.2f}".replace('.', ',')
