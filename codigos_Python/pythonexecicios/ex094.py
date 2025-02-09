conjuto = list()
pessoas = dict()
esc = ''
soma = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Digite o nome: ")).strip().title()
    pessoas['sexo'] = str(input("informe o sexo M (masculino) OU F (femino): ")).strip().upper()
    while pessoas['sexo'] not in 'MmFf':
        print("erro.")
        pessoas['sexo'] = str(input("informe o sexo M (masculino) OU F (femino): ")).strip().upper()
    pessoas['idade'] = int(input("Digite a idade: "))
    soma += pessoas['idade']
    conjuto.append(pessoas.copy())
    esc = str(input("deseja adicionar outra pessoa S (sim) OU N (não): ")).upper()
    while esc not in "SN":
        esc = str(input("deseja adicionar outra pessoa S (sim) OU N (não): ")).upper()
    if esc == "N":
        break
media = soma / len(conjuto)
print("-=" * 20)
print(f"A quantidade de pessoas cadastradas foram {len(conjuto)}.")
print(f"A idade media do grupo é {media} anos.")
print("-=" * 20)
print("-  Lista de mulheres digitadas.")
for k in conjuto:
    if k['sexo'] == "F":
        print(k['nome'])
print("-=" * 20)
print("- lista de pessoas com idade acima ou igual a da media.")
for k in conjuto:
    if k['idade'] >= media:
        print(f"{k['nome']} com {k['idade']} anos")