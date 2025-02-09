valores = list()
menor = maior = 0
for c in range(0, 5):
    valores.append(int(input(f'digite um valor para a posição {c}: ')))
    if c == 0:
        menor = maior = valores[c]
    else:
        if maior <= valores[c]:
            maior = valores[c]
        if menor >= valores[c]:
            menor = valores[c]
print('-='*15)
print(f'Você digitou os valores {valores}')

print(f'\no maior valore na sua lista é {maior} e sua posição é ', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}...', end='')
print(f'\no menor valor na sua lista é {menor} e sua posição é ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}...', end='')
