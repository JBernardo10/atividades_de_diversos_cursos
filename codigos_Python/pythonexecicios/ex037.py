numero = int(input("digite um número qualquer:"))
#pede um dado
#bi = bin(numero)
#oc = oct(numero)
#he = hex(numero)
#print("o número {}.\nem binario é {}.\nem octal é {}.\nem hexadecimal é {}".format(numero, bin(numero)[2:], oct(numero)[2:], hex(numero)[2:]))
#mostra o dado em binario, octal, e em hexadecimal
print("escolha uma base para conversão:"
      "[1] binario"
      "[2] octagonal"
      "[3] exadecimal")
escolha = int(input("sua escolha: "))
if escolha == 1:
    print(f"{bin(numero)}")
elif escolha == 2:
    print(f"{oct(numero)}")
elif escolha == 3:
    print(f"{hex(numero)}")
else:
    print("escolha invalida")