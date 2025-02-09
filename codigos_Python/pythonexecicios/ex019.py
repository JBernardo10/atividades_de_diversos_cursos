from random import choice #importa a biblioteca de randomização
n1 = input("digite o nome do primeiro aluno/a:")#pede um nome
n2 = input("digite o nome do segundo aluno/a:")#outro nome
n3 = input("digite o nome do terceiro aluno/a:")#outro nome
n4 = input("digite o nome do quarto aluno/a:")#outro nome
lista = [n1, n2, n3, n4]#cria uma lista
al = choice(lista)#seleciona um aletorio da lista
print("o/a esolhido/a foi:", al)# mostra o escolhido