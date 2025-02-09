todos = list()
nome = []
nota = []
while True:
    nome.append(str(input("Nome: ")))
    nota.append(float(input("Nota 1: ")))
    nota.append(float(input("Nota 2: ")))
    nota.append((nota[0]+nota[1])/2)
    nome.append(nota[:])
    todos.append(nome[:])
    nome.clear()
    nota.clear()
    if str(input("Deseja contunuar [s/n]: ")).lower() == 'n':
        break
print("-="*15)
print(f'{"No.": <5}{"Nome": >5}{"media": >15}')
print("-"*30)
for c, d in enumerate(todos):
    print(f'{c: <5}{d[0]: <5}{d[1][2]: >15}')
print("-"*30)
while True:
    print("para para digite '999'")
    n = int(input("mostrar as notas de qual aluno: "))
    if n == 999:
        break
    print(f"As notas de {todos[n][0]} são {todos[n][1][0]}, {todos[n][1][1]}\n")