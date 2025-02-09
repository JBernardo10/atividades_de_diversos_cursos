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


def resumo(preco=0, txA=10, txR=10):
    '''

    :param preco: um valor a ser calculado
    :param txA: uma taxa de aumento a ser incrementada no preço
    :param txR: uma taxa de redução a ser incrementada no preço
    :return: sem retorno
    '''
    print("_"*30)
    print("RESUMO DO VALOR".center(30))
    print("_"*30)
    print(f"Preço analisado: {moeda(preco):>16}")
    print(f"O dobro do preço: {dobro(preco, True):>15}")
    print(f"Metade do preço: {metade(preco, True):>16}")
    print(f"Com {txA}% de aumento: {aumentar(preco, txA, True):>13}")
    print(f"Com {txR}% de redução: {diminuir(preco, txR, True):>13}")
    print("_"*30)