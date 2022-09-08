def fatorial(n, boolean=False):
    '''
    -> Calcula o fatorial de um número
    :param n: numero do fatorial
    :param boolean: Verdadeiro para mostrar a conta, falso para mostrar apenas o resultado
    :return:
    '''
    cont = 1
    for n in range(n, 0, -1):
        cont *= n
        if boolean == True:
            if n > 1:
                print(f'{n} x ', end='')
            else:
                print(f'{n} = ', end='')
    print(cont)

fatorial(5, True)