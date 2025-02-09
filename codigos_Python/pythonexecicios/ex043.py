peso = float(input("digite o seu peso:"))#pede um dado
alt = float(input("digite sua altura:"))#pede um dado
ima = (alt ** 2)#calcula o quadrado de um dado
imc = peso / ima#calcula o imc
if imc < 18.5:
    print("seu IMC é de {:.2f}, aparentemente vc está abaixo do ideal que"
          " é entre 18,5 e 25, ou seja vc está abaixo do peso.".format(imc))
elif 18.5 <= imc <= 25:
    print("seu IMC é de {:.2f} e está na média, parabéns".format(imc))
elif 25 < imc <= 30:
    print(' seu IMC é {:.2f}, e está acima do ideal, você apresenta sobrepeso'.format(imc))
elif 30 < imc <= 40:
    print(' seu IMC é {:.2f}, e está acima do ideal, você apresenta obesidade'.format(imc))
elif imc > 40:
    print("seu IMC é {:.2f}, e está acima do ideal, você apresenta obesidade morbida.\n busque ajuda "
          "medica/nutricional".format(imc))
#testa o imc da pessoa
print("o imc ideal é entre 18,5 e 25.")
