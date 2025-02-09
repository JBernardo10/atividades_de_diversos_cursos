nota1 = float(input("digite a primeira nota:"))#pede um dado
nota2 = float(input("digite a segunda nota:"))#pede um dado
media = (nota1 + nota2) / 2#calcula a media
if media < 5:#compara
    print("Você foi reprovado!")
elif 5 <= media < 6.9:#compara
    print("Você ficou de recuperaçâo.")
elif media >= 7:#compara
    print("Você foi aprovado!")
print(media)
