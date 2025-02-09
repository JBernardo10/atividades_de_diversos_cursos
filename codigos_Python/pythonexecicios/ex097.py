def escreva(texto):
    tamanho = len(texto)
    lin(tamanho + 4)
    print(f"{texto:>{tamanho + 2}}")
    lin(tamanho + 4)

def lin(tam):
    print("~"*tam)

#programa principal
escreva("dudu")
escreva("jaize amor")