numero = int(input("Digite um número para ver sua tabuada: "))
for c in range(1,11):
    print("{} x {} = {}".format(numero, c, numero * c))
print("Fim")