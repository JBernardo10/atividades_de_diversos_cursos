jogad = dict()
todos = list()
par = 0
while True:
    jogad['nome'] = str(input("nome do jogador: "))
    par = int(input("partidas jogadas: "))
    aprovei = list()
    aux = 0
    tot = 0
    for c in range(par):
        aprovei.append(int(input(f"saldo de gols na partida {c+1}: ")))
        tot += aprovei[c]
    jogad['aproveitamento'] = aprovei.copy()
    jogad['total'] = tot
    todos.append(jogad.copy())
    if str(input("deseja adicionar outro jogador s/n: ")) in "Nn":
        break
del jogad
print(todos)
print("=-="*12)
print(f"{'cod':>3} {'nome':<10}{'jogos':<10}{'gols':<10}")
print("-"*40)
for p, i in enumerate(todos):
    print(f"{p:>3} ", end='')
    for d in i.values():
        print(f"{str(d):<10}", end='')
    print('')
print("-"*40)
while True:
    cod = int(input("mostrar dados de qual jogador: "))
    if 0 <= cod < len(todos):
        print("-="*30)
        print(f"levantamento do jogador {todos[cod]['nome']}")
        print("-"*60)
        for p in range(len(todos[cod]['aproveitamento'])):
            print(f"no jogo {p+1} fez {todos[cod]['aproveitamento'][p]} gols")
    else:
        print("erro, escolha um codigo valido")
    sair = str(input("\ndeseja sair? s/n: ")).strip().lower()
    if sair == "s":
        break
