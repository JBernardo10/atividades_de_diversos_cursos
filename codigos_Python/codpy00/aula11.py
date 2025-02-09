#colorindo o python
print('\033[34mola joao\033[m')
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33',
    'pretobranco':'\033[7;30',
    'vermelho':'\033[31m',
    'verde':'\033[32m'}
print("o {}mundo{} está {}muito{} bonito {}hoje{}"
      .format(cores['azul'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['verde'], cores['limpa']))
