decimo = pa0 = int(input('digite o primeiro valor: '))
pa1 = int(input('digite a razão: '))
c=10
while c != 0:
    print(decimo, end='...')
    decimo += pa1
    c-=1
    if c==0:
        c=int(input("\nvoce ainda deseja ver quantos termos a mais? saco deseje sair digite [0]:  "))
print("acabou")