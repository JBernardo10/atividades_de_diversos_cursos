print("olá, aqui é um gerenciador de emprestimos para compra de imóveis.")#mensagem
nome = str(input("poderia nos informar qual o seu nome:"))#pede um dado
valor = float(input("o senhor/a {} deseja comprar um imóvei de qual valor?".format(nome)))#pede um dado
sala = float(input("agora nos informe qual o valor do seu salário:"))#pede um dado
anos = float(input("em quantos anos o senhor/a {} deseja pagar esse emprestimo?".format(nome)))#pede um dado
s30 = sala * 3/10#calcula 30%do salario
prestacao = valor / (anos * 12)#calcula o valor da prestação
print("{}, o valor da prestação ficará R${:.2f}/mês".format(nome, prestacao))
if prestacao > s30:#testa se a prestação é suficiente para ser paga
    print("O valor da prestação excede 30% do seu salario por mês, "
          "\n não foi possivel aprovar o seu emprestimo")
elif prestacao <= s30:#testa se pestação é cara
    print("O valor da prestação está a baixo de 30% do seu salário"
          "\n seu emrestimo foi aprovado, parabéns!")
