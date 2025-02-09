nome = input("digite o nome da sua cidade:")#pede um dado
a = nome.strip().lower().split()#formata esse dado(sem espaços inuteis, minusculo, tudo junto)
a1 = 'santo' in a[0]#busca o nome santo no que foi digitado
print(a1)