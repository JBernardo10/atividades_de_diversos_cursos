n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print(' a soma vale {}, \n o produto vale {}, \n a divisão vale {:.3f}'.format(s, m, d), end ='')
print(' a divisão interia vale {}, e a potenciação vale {}'.format(di, e))
