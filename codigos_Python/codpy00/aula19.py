estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())  # copia o
    # conteudo do dicionario sem fazer fatiamento

# print(brasil)
for e in brasil:
    print(f'O estado é {e["uf"]} a sigla '
          f'é {e["sigla"]}')
    #for v in e.values():
     #   print(f"O estado {v}, ", end="")

"""brasil = [] criando uma lista
estado1={'uf': 'Rio de Janeiro', 'sigla': 'RJ'} discinario 
estado2 = {'uf': 'Bahia', 'sigla': 'BA'} discionario
brasil.append(estado1) incluindo um discinario em uma lista
brasil.append(estado2) idem
print(estado1)
print(estado2)
print(brasil[1]['sigla'])"""
# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 20}
# pessoas['peso'] = float(input("digite seu peso"))
# for k, v in pessoas.items():
#    print(f'{k} = {v}')
# print(pessoas['nome']) mostra o nome
# print(f'o {pessoas['nome']}') da erro pois usando aspas simples
# varias vezes, teria que ser duplas
# ex: print(f"o {pessoas['nome']}")
# del(pessoas['sexo'])
# pessoas['nome']= 'bernardo'

'''filmes={'titulo': 'star wars',
        'ano': 1997,
        'diretor': 'George Lucas'
        }

print(filmes.values())
print(filmes.keys())
print(filmes.items())
del(filmes['ano'])
for k, v in filmes.items():
    print(f'o {k} é {v}')'''
