n = input('digite algo:')#pedindo a estrada de um texto
print('O tipo primitivo disso é', type(n))#diz qual o tipo do texto digitado
print('Só tem espaços?', format(n).isspace())#testa se é apenas espaços
print('É um número?', format(n).isnumeric())#testa se e numero
print('É alfabetico?', format(n).isalpha())#testa se e letra
print('É alfanumérico?', format(n).isalnum())#testa se e alfanumerico
print('Está em maiúsculo?', format(n).isupper())#testa de esta maiuculo
print('está em minúsculo?', format(n).islower())#testa se esta minusculo
print('estsá capitalizada?', format(n).istitle())#testa se a primeira letra e maiuscula
