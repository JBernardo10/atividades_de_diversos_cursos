def area(comp, larg):
    tam = comp * larg
    return tam


def lin():
    print("-"*30)


def mostrar(comp, larg, tam):
    print(f"A área do terreno {comp}x{larg} é de {tam}m²")


print(f"{'controle de terreno':<10}")
lin()
larg = float(input("largura (m): "))
comp = float(input("comprimento (m): "))
tam = area(comp, larg)
lin()
mostrar(comp, larg, tam)
