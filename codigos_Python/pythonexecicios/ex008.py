m1 = float(input('Digite uma distancia em metros:'))#pede uma distancua em metros
km = float(m1*0.001)#calcula o kilomentro
hm = float(m1*0.01)#hectomento
dam = float(m1*0.1)#decamentro
m = float(m1)#metro
dm = float(m1/0.1)#decimentro
cm = float(m1/0.01)#centimetro
mm = float(m1/0.001)#milimetro
print('A medida de {}m corresponde a \n{}km \n{}hm \n{:.1f}dam \n{}m \n{}dm \n{}cm \n{}mm '.format(m, km, hm, dam, m, dm, cm, mm))
#mostra cada lavor
