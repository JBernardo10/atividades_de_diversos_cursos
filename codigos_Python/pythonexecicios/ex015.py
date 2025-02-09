#calcula o valo de empretimo de um carro
d = int(input('quantos dias o carro foi alugado?'))
k = float(input('quantos KM foram rodados?'))
vp = (d * 60) + (k * 0.15)#calcula o valor final a pagar
print('O total a pagar é de R${:.2f}'.format(vp))#mostra o valor final
