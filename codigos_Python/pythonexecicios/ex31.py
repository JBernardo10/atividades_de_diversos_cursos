via = int(input("qual a distância da sua viagem em km?"))#pede um dado
if via <= 200:#compara se é menor ou igual
    a = via * 1/2#executa um calculo
#print("O valor cobrado para essa distância de {}km é R${}".format(via, a))
else:#se a condição acima for falsa
    a = via * 45/100#executa o calculo
print("O valor cobrado para essa distância de {}km é R${}".format(via, a))#mostra o resultado
#preço = via * 0.50 if via<=200 else via * 0.45