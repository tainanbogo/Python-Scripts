print("++++ Lojas Guanabara ++++")
valor = float(input('Preço das Compras: R$ '))
print("++++ Formas de Pagamento ++++\n"
      "[1] Á vista (Dinheiro/Cheque)\n"
      "[2] Á vista (Cartão)\n"
      "[3] 2x no Cartão\n"
      "[4] 3x ou mais no Cartão")
opcao = int(input('Qual sua opção? '))

if opcao == 1:
    valorfinal = valor * 0.9
    print('Você ganhou 10% de desconto! Sua compra de {} sairá por {}'.format(valor, valorfinal))
elif opcao == 2:
    valorfinal = valor * 0.95
    print('Você ganhou 5% de desconto! Sua compra de {} sairá por {}'.format(valor, valorfinal))
elif opcao == 3:
    print("Para esta opção não oferecemos desconto!\n"
          "Sua compra sairá por R${} dividida em 2x de R${}".format(valor, valor/2))
elif opcao == 4:
    parcelas = int(input("Quantas Parcelas? "))
    valorfinal = valor * 1.2
    valorparcelas = valorfinal / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!\n'
          'Sua compra de R${} vai custar R${} no final.'.format(parcelas, valorparcelas, valor, valorfinal))
else:
    print('Opção Inválida de pagamento! Tente Novamente!')