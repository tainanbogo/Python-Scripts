def maior(*num):
    lista = list()
    print(f'Analisando os valores passados...')
    for i in num:
        lista.append(i)
        print(f'{i}', end=' ')
    print(f'Foram informados {len(lista)} valores.')
    lista.sort()
    print(f'O maior valor da lista é {lista[-1]}')

maior(1, 2, 3, 6, 0, 20, 0, 8)
