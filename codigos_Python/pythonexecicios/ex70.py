total = totilmil = menor = cont = 0
barato = ''
while True:
    produto = str(input("nome do produto: "))
    preco = float(input("preço R$: "))
    cont+=1
    total += preco
    if cont ==1 or preco<menor:
        menor = preco
        barato = produto
    if preco>1000:
        totilmil+=1
    resp = ' '
    resp = str(input("quer continuar? [S/N]: ")).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('fin do programa'))
print(f"o total da compra foi R${total:.2f}")
print(f"{totilmil} custava mais de mil reis")
print(f'o produto mais barato foi {barato} e custa R$ {menor:.2f}')