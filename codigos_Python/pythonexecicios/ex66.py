n=cont=s=0
while True:
    n=int(input("digite um valor"))
    if n==999:
        break
    cont+=1
    s+=n
print(f'vc digitou {cont} valore e sama entre eles e {s}')