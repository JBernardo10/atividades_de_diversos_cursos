from datetime import date
#calcula a idade e mostra asituação de voto
def voto(nascimento):
    global idade
    idade = date.today().year - nascimento
    if idade < 16:
        return f'Com {idade} anos, o voto é NEGADO'
    elif idade < 18 or idade >= 60:
        return f'Com {idade} anos, o voto é OPCIONAL'
    else:
        return f'Com {idade} anos, o voto é OBRIGATORIO'


nascimento = int(input("Em que ano você nasceu: "))
situacao = voto(nascimento)
print(situacao)

