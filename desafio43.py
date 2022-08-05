peso = float(input('Qual seu peso(kg): '))
altura = float(input('Qual sua altura(m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.2f}. ABAIXO DO PESO!'.format(imc))
elif imc < 25:
    print('Seu IMC é de {:.2f}. PESO IDEAL!'.format(imc))
elif imc < 30:
    print('Seu IMC é de {:.2f}. SOBREPESO!'.format(imc))
elif imc < 40:
    print('Seu IMC é de {:.2f}. OBESIDADE!'.format(imc))
else:
    print('Seu IMC é de {:.2f}. OBESIDADE MÓRBIDA!'.format(imc))
