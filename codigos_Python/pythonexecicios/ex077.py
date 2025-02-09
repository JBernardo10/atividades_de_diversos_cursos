palavras = ('joao', 'jose', 'ferreira', 'casa', 'mouse',
            'janela', 'porta', 'parede', 'branco', 'mesa',
            'alto', 'mosquito', 'montanha', 'bonita')
for p in palavras:
    print(f'\nna palavra "{p}" temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')