soma = 0
maior = 0
velho = ""
totm = 0
for c in range(1, 5):
    print("--- {}ª Pessoa ---".format(c))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("[M/F]: "))
    soma = soma + idade
    if sexo == "M":
        if idade > maior:
            maior = idade
            velho = nome
    else:
        if sexo == "F" and idade < 20:
            totm = totm + 1


print("A média de idade do grupo é de {}".format(soma/4))
print("O homem mais velho tem {} anos e se chama {}".format(maior, velho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(totm))
