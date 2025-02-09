contmaior = conthom = contm20 = 0

while True:
    print('-'*15)
    print("cadastrar uma pessoas ")
    print('-'*15)
    idade = int(input("idade: "))
    sexo = str(input("sexo [M/F]: ")).upper().strip()[0]
    print('-' * 15)
    while sexo not in 'MF':
        sexo = str(input("resposta invalida, digite seu sexo [M/F]: ")).upper()

    if idade >= 18:
        contmaior+=1
    if sexo == 'M':
        conthom+=1
    if sexo == 'F' and idade < 20:
        contm20+=1
    continuar = str(input("quer continuar [S/N]: ")).strip().upper()[0]
    while continuar not in 'SN':
        print("resposta invalida!")
        continuar = str(input("quer continuar [S/N]: ")).upper().strip()[0]
    if continuar == 'N':
        break
print(f"o total de pessoas com mais de 18 anos foi de {contmaior}\n"
      f"ao todo temos {conthom} homens cadastrados\n"
      f"e temos {contm20} mulheres com menos de 20 anos")
