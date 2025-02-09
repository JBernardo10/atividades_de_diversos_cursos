def ficha(nom = 'desconhecido', gol = 0):
    """
    :param nom: nome do jogador
    :param gol: total de gols realizados
    :return: sem retorno
    """
    #if nom == '':
    #    nom = "<desconhecido>"
    #if gol == '':
    #    gol = '0'
    print(f"o jogador {nom}, fez {gol} gols no campeonato")


#nome = str(input("nome do jogador: "))
#gols = str(input("numero de gols: "))
#ficha(nome, gols)


nome = str(input("nome do jogador: "))
gols = str(input("numero de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)