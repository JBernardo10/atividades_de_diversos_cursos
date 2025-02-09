valor = float(input("digite o valor do produto:"))#pede um valor
forma = int(input("digite a forma de pagamento.\n"
                  "[ 0 ] para pagamento a vista, 10% de desconto.\n"
                  "[ 1 ] para pagamento a vista no cartão, 5% de desconto.\n"
                  "[ 2 ] para parcelado em 2 vezes no cartão, valor real do produto.\n"
                  "[ 3 ] para parcelado mais de 3 vezes no cartâo, 20% de juros.\n"))#mostra o menu
if forma == 0:
    vd = valor - (valor * 10/100)
    print("o valor pago será R${:.2f}.".format(vd))
elif forma == 1:
    vd = valor - (valor * 5/100)
    print("o valor pago será R${:.2f}.".format(vd))
elif forma == 2:
    vd = valor / 2
    print("o valor pago será duas parecelas de R${:.2f}.".format(vd))
elif forma == 3:
    np = int(input("digite o numero de parcelas: "))
    vd = ((valor * 20/100) + valor) / np
    print("o valor de cada parela será R${}".format(vd))
else:
    print("opção invalida de pagamento, tente novamente!")
#compara e calcula de acordo a forma de pagamento