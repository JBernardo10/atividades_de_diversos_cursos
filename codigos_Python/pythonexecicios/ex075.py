num = (int(input('digite um numero: ')), int(input('digite outro numero: ')),
       int(input('digite mais um numero: ')), int(input('digite o ultimo numero: ')))
print(f'você digitou os valores {num}')
print(f'o valor 9 apreceu {num.count(9)} vezes')
if 3 in num:
       print(f'o valor 3 apareceu na {num.index(3)+1}ª oposição')
else:
       print("o valor 3 nao foi digitado.")
print('os numeros pares digitados foram: ')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')