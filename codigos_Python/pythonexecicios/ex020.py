from random import shuffle#importa a biblioteca
n1 = input("digite o nome do primeiro aluno/a:")#pede um nome
n2 = input("digite o nome do segundo aluno/a:")# outro nome
n3 = input("digite o nome do terceiro aluno/a:")#outro nome
n4 = input("digite o nome do quarto aluno/a:")#outro nome
nomes = [n1, n2, n3, n4]#cria uma lista
shuffle(nomes)#organiza uma ordem aleatoria
print("a ordem é")
print(nomes)