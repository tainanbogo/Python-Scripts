n = soma = cont = 0
n = int(input("Digite um número [999 para parar]: "))

while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um número [999 para parar]: "))

print("Você digitou {} números e a soma deles foi {}".format(cont, soma))
print("FIM!")
