print('--- Cadastre uma pessoa! ---')
mais18 = 0
homem = 0
mulher = 0
total = 0
while True:
    p = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ').upper().strip()[0])
    print('-=' * 20)
    if p > 18:
        mais18 += 1
    if s == 'M':
        homem += 1
    if s == 'F' and p < 20:
        mulher += 1
    total += 1
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer Continuar? [S/N]').upper().strip()[0]
    if cont == 'N':
            break
print(f'Você cadastrou {total} pessoas.\n'
      f'Temos {mais18} pessoas com mais de 18 anos\n'
      f'{homem} homens cadastrados e {mulher} mulheres com menos de 20 anos.')

