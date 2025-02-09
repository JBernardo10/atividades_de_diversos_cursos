vel = int(input("Qual a velocidade do carro?"))#pede um dado
if vel > 80:#faz uma comparação
    mul = (vel - 80) * 7#executa um calculo da multa
    print("Voçê excedeu o limite de velocidae permitdo de 80km/h."
          "\nAgora voçê deve pagar uma multa no valor de R${}.".format(mul))#mostra o resultado
print("tenha um bom dia dirija com segurança")
