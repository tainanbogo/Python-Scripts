n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("O PRIMEIRO número, {}, é maior que {}!".format(n1, n2))
elif n2 > n1:
    print("O SEGUNDO número, {}, é maior que {}".format(n2, n1))
else:
    print("Não existe valor maior ou menor, os valores {} e {} são iguais!".format(n1, n2))
