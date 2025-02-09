def leiaInt(msg):
    while True:
        dado = input(f"{msg}")
        if dado.isnumeric():
            return int(dado)
        else:
            print('\033[31mERRO! digite um numero inteiro válido\033[m')
        '''try:
            valor = int(dado)
            break
        except:
            print('\033[31mERRO! digite um numero inteiro válido\033[m')
    return valor'''


n = leiaInt('digite um numero: ')
print(f"o valor digitado é {n}")