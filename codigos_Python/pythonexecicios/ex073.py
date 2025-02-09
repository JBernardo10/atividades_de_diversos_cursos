print("lista dos times do brasileirão 2023 por classificação")

TBclassificacao = ('Botafogo', 'Palmeiras', 'Fluminense', 'Cruzeiro', 'Atheletico-PR',
                   'Atletico-MG', "Santos", 'Fortaleza', 'Flamengo', 'São paulo', 'Gremio',
                   'Internacional', 'Bragatino', 'Bahia', 'Goias', 'vasco da Gama', 'Corinthians',
                   'Cuiaba', 'Coritiba', 'America -MG')
print("-="*10)
print(f"Lista de times: tb{TBclassificacao}")
print("-="*10)
print(f'Os 5 primeiros times são: {TBclassificacao[0:5]}')#mostra da posição 0 a 4, ignorando a 5
print("-="*10)
print(f'os 4 ultimos classificados são: {TBclassificacao[-4:]}')#inicia a contagem de tras apartir do elemento -4
print("-="*10)
print(f'os times em ondem alfabetica são: {sorted(TBclassificacao)}')
print("-="*10)
print(f"o Bahia está na posição {TBclassificacao.index('Bahia')+1}")