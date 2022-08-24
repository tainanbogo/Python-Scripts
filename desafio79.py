lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Número repetido. Digite outro.')
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'Nn':
        break
lista.sort()
print(f'Os valores adicionados foram {lista}')