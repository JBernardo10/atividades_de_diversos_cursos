print('-'*22)
print("sequencia de Fibonacci")
print('-'*22)
n = int(input("digite quantos  numeros vc quer ver: "))
t1 = 0
t2 = 1
cont=0
print("{}...{}...".format(t1, t2), end='')
while cont < n-2:
    t3 = t1+t2
    print(t3, end='...')
    t1 = t2
    t2 = t3
    cont+=1
print("\nfim")