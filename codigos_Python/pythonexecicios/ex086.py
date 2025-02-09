matriz = [[], [], []]
print("Preencha a matriz\n"
      "  1     2     3\n"
      "1 []    []    []\n"
      "2 []    []    []\n"
      "3 []    []    []\n")
print('-='*15)
somapar = somaterc = maiorsegl = 0
for c in range(0, 3):
    for a in range(0, 3):
        matriz[c].append(int(input(f"digite um valor para a posição [{a + 1}, {c + 1}]: ")))
        if matriz[c][a] % 2 == 0:
            somapar += matriz[c][a]
        if a == 2:
            somaterc += matriz[c][a]
        if c == 1:
            if maiorsegl < matriz[1][a]:
                maiorsegl = matriz[c][a]
print('-='*15)
print("Matriz preenchida")
for c in matriz:
    print(f'[{c[0]:^5}] [{c[1]:^5}] [{c[2]:^5}]\n')
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somaterc}')
print(f"o maior valor da segunda linha é {maiorsegl}")
