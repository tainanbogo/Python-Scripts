numero = int(input('Escreva um número qualquer: '))
print("*" * 10)
print("Escolha uma das bases para conversão:\n"
      "[1] Converter para BINÁRIO\n"
      "[2] Converter para OCTAL\n"
      "[3] Converter para HEXADECIMAL")
escolha = int(input('Sua opção: '))

if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(numero, hex(numero)[2:]))
else:
    print('Não entendi sua escolha, por favor digite novamente!')
