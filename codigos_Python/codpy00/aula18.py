'''teste = list()
teste.append('joao')
teste.append(20)
galera = list()
galera.append(teste[:])
print(galera)
teste[0] = 'maria'
teste[1] = 25
galera.append(teste[:])
print(galera)'''
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('nome: ').capitalize()))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] > 18:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')