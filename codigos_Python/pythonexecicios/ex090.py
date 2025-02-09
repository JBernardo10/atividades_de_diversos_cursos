'''aluno1 = {}
# aluno1 = {'nome': str(input("digite o nome do algor: ")).strip(), 'media': float(input("digite a média: "))}
aluno1['nome'] = str(input("digite o nome do aluno: ")).strip()
aluno1['media'] = float(input("digite a média: "))
if aluno1['media'] >= 7:
    aluno1['situa'] = "aprovado"
elif 5 <= aluno1['media'] < 7:
    aluno1['situação'] = "recuperação"
else:
    aluno1['situa'] = "reprovado"
print(f"O nome é igual a {aluno1['nome']}\nA média é {aluno1['media']}\n"
      f"Situação é {aluno1['situa']}")'''

aluno2 = dict()
aluno2['nome'] = str(input("digite o nome do aluno: ")).strip().title()
aluno2['media'] = float(input(f"media de {aluno2['nome']}: "))
if aluno2['media'] >= 7:
    aluno2['situa'] = "Aprovado"
elif 5 <= aluno2['media'] > 7:
    aluno2['situa'] = "Recuperação"
else:
    aluno2['situa'] = "reprovado"

print(f"Nome do aluno: {aluno2['nome']}\n"
      f"Media: {aluno2['media']}\n"
      f"Situação: {aluno2['situa']}\n")