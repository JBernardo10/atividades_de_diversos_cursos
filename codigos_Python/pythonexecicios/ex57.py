sexo = str(input("digite seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in 'MmFf':
   sexo = str(input("dados invalidos, por favor informe seu sexo: ")).strip().upper()[0]

print("sexo {} informado com sucesso".format(sexo))
print("saiu")