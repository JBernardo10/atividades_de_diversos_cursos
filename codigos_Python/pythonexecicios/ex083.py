expr = str(input('digite uma espressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append("(")
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('sua expressão esta correta.')
else:
    print('sua expressão está errada.')