numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(len(numeros))
#n = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
#escolha = int(input('digite um valor de 0 a 20: '))
#while escolha not in n: #MEU jeito
 #   escolha = int(input("opição invalida, digite uma valor entre 0 e 20: "))
#if escolha in n:
 #   print(f"voce digitou o numero {numeros[escolha]}")
print("saiu")
# outro jeito
while True:
    num = int(input("digite um numero de 0 a 20: "))
    if 0 <= num <= 20:
        break
    print("tente novamente,", end=' ')
print(f"o numero digitado foi {numeros[num]}")