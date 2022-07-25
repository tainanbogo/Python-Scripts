n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
lista = sorted([n1, n2, n3])
print('Você digitou os números: {} \n'
      'O menor valor é: {}\n'
      'O maior valor é: {}'.format(lista, lista[0], lista[2]))


