todos = list()
pessoa = list()
while True:
    pessoa.append(str(input("Nome: ").capitalize()))
    pessoa.append(float(input("Peso: ")))
    todos.append(pessoa[:])
    pessoa.clear()
    if str(input('Deseja adicionar outra pessoa?[S/N]: ')) in 'nN':
        break
print('-='*20)
print(f'Ao total foram cadastradas {len(todos)} pessoas')
print(f'As pessoas mais pesadas (70kg ou acima) são: ', end='')
for p in todos:
    if p[1] >= 70:
        print(f'{p[0]}, ', end='')
print(f'\nE as pessoas mais leves (60 ou abaixo) são: ', end='')
for p in todos:
    if p[1] <= 60:
        print(f'{p[0]}, ', end='')
