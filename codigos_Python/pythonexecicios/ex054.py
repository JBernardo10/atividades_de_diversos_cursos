from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    p1 = int(input("em que a ano a {} pessoa nasceu?".format(pess)))
    idade = atual - p1
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print("ao todo tivemos {} pessoas maior de idade"
      "\ne também {} pessoas menores de idade".format(totmaior, totmenor))
