from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'aquivoDados.txt'

if not arquivoExiste(arq):
    criarAquivo(arq)

while True:
    resposta = menu(["mostrar pessoas cadastradas",
                     "cadastrar nova pessoa", "sair dos sistema"])
    if resposta == 1:
        #mostra o conteudo do arquivo
        lerAquivo(arq)
    elif resposta == 2:
        #cadastra uma nova pessoa
        cabecalho("NOVO CADASTRO")
        nome = str(input("nome: "))
        idade = leiaInt("idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("saindo do sistema...")
        break
    else:
        print("\033[31mERRO\033[m, digite uma opção valida.")
    sleep(1)