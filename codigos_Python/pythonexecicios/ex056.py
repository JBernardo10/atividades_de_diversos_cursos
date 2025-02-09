somaidade = 0
mediaidade = 0
maiorhomen = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print('-----{}ª pessoa -----'.format(p))
    nome = str(input('nome: ')).strip()
    idede = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()
    somaidade += idede
    if p == 1 and sexo in 'Mm':
        maiorhomen = idede
        nomevelho = nome
    if sexo in 'Mn' and idede > maiorhomen:
        maiorhomen = idede
        nomevelho = nome
    if sexo in 'Ff' and idede < 20:
        totmulher += 1

mediaidade = somaidade / 4
print("a media da idade do grupo é de {} anos".format(mediaidade))
print("o homem mais velho se chama {} e sua idade é {} anos".format(nomevelho,maiorhomen))
print("ao todo sao {} mulheres com menos de 20 anos".format(totmulher))
