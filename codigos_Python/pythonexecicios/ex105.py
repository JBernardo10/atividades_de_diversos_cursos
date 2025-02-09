def notas(*n, situa = False):
    """
    :param n: um conjuto de valores
    :param situa: opcinal, mostra a cituação da media
    :return: um dicionario com os valores trabalhados
    """
    conjunto = dict()
    conjunto['total'] = len(n)
    conjunto['maior'] = max(n)
    conjunto['menor'] = min(n)
    conjunto['media'] = sum(n)/len(n)
    '''conjunto['total'] = 0
    conjunto['maior'] = n[0]
    conjunto['menor'] = n[0]
    tot = 0
    for v in n:
        conjunto['total'] +=1
        if conjunto['menor'] > v:
            conjunto['menor'] = v
        if conjunto['maior'] < v:
            conjunto['maior'] = v
        tot += v
    conjunto['media'] = tot / conjunto['total']'''
    if situa:
        if conjunto['media'] <= 4:
            conjunto['situa'] = 'ruim'
        elif conjunto['media'] <= 6:
            conjunto['situa'] = 'regular'
        else:
            conjunto['situa'] = 'boa'
    return conjunto


n = notas(2,8, situa=True)
print(n)