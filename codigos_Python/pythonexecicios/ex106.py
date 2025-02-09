cores = ('\033[m', #0 sem cor
        '\033[0;31;44m', #1 vermelho e verde
         '\033[0;34;40m', #2 azul e preto
         '\033[4;33m', #3 marron e vermelho
        )

from time import sleep
def ajuda(comando):
    titulo(f'acessando o manual do comando \'{comando}\'', 1)
    print(cores[2], end='')
    help(comando)
    print(cores[0], end='')
    sleep(2)



def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(cores[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYhelp', 1)
    print(cores[3])
    comando = str(input("função ou biblioteca > "))
    print(cores[0])
    if comando.strip().lower() == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO', 1)