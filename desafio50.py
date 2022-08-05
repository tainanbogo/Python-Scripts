soma = 0
cont = 0
for c in range(1,7):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        soma = soma + numero
        cont = cont + 1
print("Você informou {} números pares e a soma deles é igual a {}".format(cont, soma))