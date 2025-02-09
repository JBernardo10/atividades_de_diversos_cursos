a = float(input('qual a altura da parede?'))#pede as dimensoes de uma parede
c = float(input('qual a largura da parede?'))
m2 = a*c#calcula a area da parede
qt = m2*(1/2)#calcula a quantidade de tinta que usaria para pintar
print(' sua parede tem a dimensão de {}x{} e sua area total é de {:.2f}m²'.format(a, c, m2))#mostra a area
print('você precisará de {}l de tinta para pintar ela.'.format(qt))#mostra a quantidade de tinta
