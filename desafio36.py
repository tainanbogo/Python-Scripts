valor = float(input('Valor da casa? R$'))
salario = float(input('Salário do comprador? R$'))
anos = int(input('Tempo para pagamento em ANOS: '))

prestacao = valor / (anos * 12)
porcentagem = salario * 0.3


if prestacao > porcentagem:
    print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}. '
          'Empréstimo NEGADO!'.format(valor, anos, prestacao))
else:
    print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}. '
          'Empréstimo CONCEDIDO!'.format(valor, anos, prestacao))

