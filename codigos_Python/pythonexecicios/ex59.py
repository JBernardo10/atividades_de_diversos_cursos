valor1 = int(input("digite o primeiro valor: "))
valor2 = int(input("digite o segundo valor: "))
ficar = 4
while ficar !=5:
    ficar = int(input("que operação deseja realizar:"
          "\n[1] para soma"
          "\n[2] para multiplicar"
          "\n[3] para saber quem é o maior"
          "\n[4] para digitar novos valores"
           "\n[5] para sair"))
    if ficar ==1:
        resultado = valor1 + valor2
        print("o resultado e {}".format(resultado))
    elif ficar == 2:
        resultado = valor1*valor2
        print("o resultado e {}".format(resultado))
    elif ficar == 3:
        if valor1> valor2:
            maior = valor1
        else: maior=valor2
        print("o maior valor e {}".format(maior))
    elif ficar == 4:
        valor1 = int(input("digite o primeiro valor: "))
        valor2 = int(input("digite o segundo valor: "))


print("saiu")