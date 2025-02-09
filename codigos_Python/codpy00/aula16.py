lanche = ('hanburger','batata frita', 'suco', 'pizza', 'pudin', 'jaize')
a = (2, 5, 7)
b = (5, 9, 7, 1)
for cont in range(0, len(lanche)):
   print(f"eu vou comer {lanche[cont]}")
print(" \n")
 #tuplas sao imutaveis
for pos, comida in enumerate(lanche):
   print(f'eu vou comer {comida}, na posicão {pos}')
for comida in lanche:
   print(f"eu vou comer {comida}")
print(sorted(lanche)) #mostra o lance em hordem
c = a + b
print(c)
#print(c.count(7))
del(c)
print(c.index(7, 3))
print("saiuk")
