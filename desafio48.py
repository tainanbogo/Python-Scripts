soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = c + soma
print("A soma entre os {} números é {}".format(cont, soma))
