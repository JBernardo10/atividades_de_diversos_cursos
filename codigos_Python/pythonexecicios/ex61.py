print('-='*10)
print("gerador de PA")
print('-='*10)

decimo = pa0 = int(input('digite o primeiro valor: '))
pa1 = int(input('digite a razão: '))
c=1
while c <= 10:
    print(decimo, end='...')
    decimo += pa1
    c+=1

print("\nacabou")