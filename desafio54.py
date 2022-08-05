from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))
    if date.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print("Nessa lista existem {} pessoas maiores de idade e {} pessoas menores de idade".format(maior, menor))
