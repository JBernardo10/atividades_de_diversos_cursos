#import math ........ a funçao radians() converte o valor para graus radianos
import math as m#importa a biblioteca
angulo = float(input("digite o angulo:"))#pede um dado
seno = m.sin(m.radians(angulo))#usa a função seno da biblioteca
print("o angulos de {} tem o seno de {:.2f}".format(angulo, seno))#mostra os dados
cosseno = m.cos(m.radians(angulo))#usa a função para calcular o cosseno
print("o angulo de {} tem o cosseno de {:.2f}".format(angulo, cosseno))#mostra os dados
tangente = m.tan(m.radians(angulo))#calcula a tengente
print("o angulo de {} tem a tangente de {:.2f}".format(angulo, tangente))#mostra os dados