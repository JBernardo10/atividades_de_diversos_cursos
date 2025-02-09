nome = str(input("digite seu nome completo:")).strip()#retira os espaços inuteis
print("seu nome em maiúscula é {}".format(nome.upper()))#poe o nometodo em maiuscula
print("seu nome em minusculas é {}".format(nome.lower()))#coloca em minuscula
a = nome.split()#forma uma lista com o nome
print("seu nome ao todo tem {} letras".format(len(nome) - nome.count(' ')))#conta quantas letras tem no nome
print(a)
#print("seu nome ao todo tem {} letras".format(len(''.join(a))))
print("seu primeiro nome tem {} letras".format(nome.find(' ')))#informa quanas letras tem o primeiro nome
#print(len(a[0]))
