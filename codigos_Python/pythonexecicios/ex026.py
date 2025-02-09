frase = str(input("digite uma frase:")).strip().lower()#pede uma frase, tira os espaços inuteis e coloca em minusculo

print("A letra 'a' apaece {} vezes na frase".format(frase.count('a')))#conta a repetição de uma letra

print("A primeira letra 'a' apareceu na posição {}".format(frase.find('a')+1))#mostra a posição da promeira letra 'a'

print("A ultima letra 'a' apareceu na posição {}".format(frase.rfind('a')+1))#mostra a posição da ultima letra 'a'
