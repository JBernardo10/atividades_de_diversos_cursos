nome = str(input("digite o seu nome completo:"))#pede um nome
n = nome.split()#cria uma lista com o nome
print(n)
print("prazer em te conhecer"
      "\nseu primeiro nome é {}"
      "\nseu ultimo nome é {}"
      .format(n[0], n[len(n)-1]))#mostra os dados
