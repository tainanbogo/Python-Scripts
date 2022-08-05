n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
opcao = 0
while opcao != 5:
    print("=" * 10)
    opcao = int(input("[1] Somar\n"
                  "[2] Multiplicar\n"
                  "[3] Maior\n"
                  "[4] Novos Números\n"
                  "[5] Sair do Programa\n"
                  "Qual a sua opção? "))
    if opcao == 1:
        print("O resultado de {} + {} = {}".format(n1,n2, n1 + n2))
    elif opcao == 2:
        print("O resultado de {} x {} = {}".format(n1,n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print("O número {} é maior que {}".format(n1,n2))
        else:
            print("O número {} é maior que {}".format(n2, n1))
    elif opcao == 4:
        print("Digite novos números: ")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
       print("Opção inválida, tente novamente!")

print("Você escolheu sair do programa! Até a próxima!")
