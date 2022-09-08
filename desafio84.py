pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print(f'Sua lista é: {pessoas}.\n'
      f'Ao todo voce cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior} KG de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}...', end='')
print()
print(f'O menor peso foi {menor} KG de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}...', end='')



