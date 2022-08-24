total = maismil = maisbarato = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip().title()
    valor = float(input('Preço: R$'))
    cont += 1
    total += valor
    if valor > 1000:
        maismil += 1
    if cont == 1:
        maisbarato = valor
        barato = produto
    else:
        if valor < maisbarato:
            maisbarato = valor
            barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'Total da compra: {total}')
print(f'Temos {maismil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} custando {maisbarato}')
