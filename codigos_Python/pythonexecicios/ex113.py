def leiaInt(msg):
    while True:
        dado = input(f"{msg}").strip()
        try:
            valor = int(dado)
        except:
            print('\033[31mERRO! digite um valor valido válido\033[m')
            continue
        else:
            return valor


def leiaFloat(msg):
    while True:
        dado = input(f"{msg}").strip()
        try:
            valor = float(dado)
        except:
            print('\033[31mERRO! digite um valor real valido válido\033[m')
            continue
        else:
            return valor


valorInt = leiaInt("digite um valor inteiro: ")
valorReal = leiaFloat("digite um valor real: ")
print(f"o valor interio digitado foi {valorInt}")
print(f"o valor real digitado foi {valorReal}")