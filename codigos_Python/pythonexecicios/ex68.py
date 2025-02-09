
from random import randint

cont = soma = valor = aleatorio = 0
print('-=' * 15)
print("vamos jogar par ou impar")
print('-=' * 15)

while True:

    valor = int(input("diga um valor: "))
    escolha = str(input("par ou impar [P/I]: ")).upper().strip()[0]

    aleatorio = randint(0, 10)
    soma = valor+aleatorio
    if soma%2 == 0 and escolha ==  'P':
        print('-'*20)
        print(f"voce jogou {valor} e computador {aleatorio}, o total de {soma} deu Par")
        print('-' * 20)
        print("voce venceu")
        print("vamos jogar novamente")
        print("-="*15)
    if soma%2 == 0 and escolha == 'I':
        print('-' * 20)
        print(f"voce jogou {valor} e computador {aleatorio}, o total de {soma} deu par")
        print('-' * 20)
        print("voce perdeu, tente novamente.")
        break
    if soma%2 == 1 and escolha ==  'P':
        print('-' * 20)
        print(f"voce jogou {valor} e computador {aleatorio}, o total de {soma} deu impar")
        print('-' * 20)
        print("voce perdeu, tente novamente.")
        break
    if soma%2 == 1 and escolha == 'I':
        print('-' * 20)
        print(f"voce jogou {valor} e computador {aleatorio}, o total de {soma} deu impar")
        print('-' * 20)
        print("voce venceu")
        print("vamos jogar novamente")
    cont += 1
print(f"GAME OVER! voce venceu {cont} vezes")