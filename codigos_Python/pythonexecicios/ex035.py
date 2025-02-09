r1 = float(input("Digite o valor da primeira reta:"))#pede um dado
r2 = float(input("Digite o valor da segunda reta:"))#pede um dado
r3 = float(input("Digite o valor da segunda reta:"))#pede um dado
'''lista = [ r1+r2>r3== r1+r3>r2== r2+r3>r1]
print(r1+r2)
print(r1+r3)
print(r2+r3)'''

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:#compara os 3 valores
    print("as medidas  formam um triangulo")#mensagem
else:
    print("as medidas nao formam um triângulo")#mensagem