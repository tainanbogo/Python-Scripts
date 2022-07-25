salario = float(input('Qual o salário do funcionário? R$'))
if salario <= 1250:
    salario = salario + (salario * 0.15)
    print('Seu novo salário com aumento de 15% será de R${:.2f}'.format(salario))
else:
    salario = salario + (salario * 0.10)
    print('Seu novo salário com aumento de 10% será de R${:.2f}'.format(salario))

