'''for c in range (1, 10)'''
'''print('c')'''
'''print(fim)'''

'''c =1
while c<11:
    print(c)
    c+= 1'''

n = 1
par = impar = 0
while n !=0:
    n = int(input("digite um valor: "))
    if n != 0:
        if n %2 ==0:
            par +=1
        else:
            impar += 1
print("os valores par sao {} e os valores impar sao {}".format(par,impar))
print("final")