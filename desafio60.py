numero = int(input("Digite um número: "))
fatorial = numero
f = 1
print("Calculando {}!".format(numero))
while fatorial > 0:
    print("{}".format(fatorial), end=" ")
    print(' x ' if fatorial > 1 else " = ", end = " ")
    f = f * fatorial
    fatorial -= 1

print(f)

