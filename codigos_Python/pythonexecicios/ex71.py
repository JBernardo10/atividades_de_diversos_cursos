'''print('='*30)
print("{:^30}".format('BANCO CEV'))
print('='*30)
valor = int(input("que valor voce quer sacar R$: "))
total = valor
ced = 50
totcedula = 0
while True:
    if total >= ced:
        total -= ced
        totcedula +=1
    else:
        if totcedula > 0:
            print(f"total de {totcedula} cedulas de R$ {ced} ")
        if ced == 50:
            ced = 20
            totcedula = 0
        elif ced == 20:
            ced = 10
            totcedula = 0
        elif ced == 10:
            ced = 1
            totcedula = 0
        if total == 0:
            break
print('='*30)
print("saiu")
print('='*30)'''
for c in range (0, 5):
    print(c)