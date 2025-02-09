r1 = float(input("Digite o valor da primeira reta:"))#pede as restas do triagulo
r2 = float(input("Digite o valor da segunda reta:"))
r3 = float(input("Digite o valor da segunda reta:"))
'''lista = [ r1+r2>r3== r1+r3>r2== r2+r3>r1]
print(r1+r2)
print(r1+r3)
print(r2+r3)'''

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:#compara se forma um triangulo
    # print("as medidas  formam um triangulo")
    if r1 == r2 == r3:#compara se todas as retas sao iguais
        print("as retas formam um triângulo equilátero.")
    elif r1 == r2 != r3 or r3 == r2 != r1 or r1 == r3 != r2:#compara se há duas retas iguais
        print("as retas formam um triângulo isósceles")
    elif r1 != r2 != r3 != r1:#compara se todas as retas são diferentes
        print("as retas formam um triângulo escaleno")
else:
    print("as medidas nao formam um triângulo")
