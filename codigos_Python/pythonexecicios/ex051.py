pa0 = int(input('digite o primeiro valor: '))
pa1 = int(input('digite a razão: '))
decimo = pa0 + (10 - 1)*pa1
for c in range(pa0, decimo+pa1, pa1):
    print('{}'.format(c), end=' ->')
print("cabou")