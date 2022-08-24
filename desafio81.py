lista = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    continuar = str(input('Deseja continuar? [S/N]: '))
    if continuar in 'Nn':
        break
    else:
        if continuar.strip().upper()[0] not in 'Ss':
            print(f'Não entendi. Digite novamente.')
            continuar = str(input('Deseja continuar? [S/N]: '))
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
    print('O valor 5 não faz parte da lista.')
else:
    print('O valor 5 faz parte da lista!')
