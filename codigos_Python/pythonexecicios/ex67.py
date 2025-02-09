while True:
    print("-"*30)
    valor = int(input("quer ver a tabuada de qual valor? "))
    print("-"*30)
    if valor <0:
        break
    else:
        cont = 0
        while cont <= 10:
            print(f"{cont} x {valor} = {cont*valor}")
            cont+=1
print("tabuada encerada")