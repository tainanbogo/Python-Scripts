# Módulo para o Desafios

def aumentar(n, taxa, formato=False):
    n = n + (n * (taxa / 100))
    return n if formato is False else dinheiro(n)


def diminuir(n, taxa, formato=False):
    n = n - (n * (taxa / 100))
    return n if formato is False else dinheiro(n)


def dobro(n, formato=False):
    n *= 2
    return n if formato is False else dinheiro(n)


def metade(n, formato=False):
    n /= 2
    return n if formato is False else dinheiro(n)


def dinheiro(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, t1=10, t2=5):
    print(f'-' * 30)
    print('Resumo de valores'.center(30))
    print(f'-' * 30)
    print(f'Preço analisado \t{dinheiro(n)}\n'
          f'Dobro do preço \t\t{dobro(n, True)}\n'
          f'Metade do preço \t{metade(n, True)}\n'
          f'{t1}% de Aumento \t\t{aumentar(n, t1, True)}\n'
          f'{t2}% de Desconto \t{diminuir(n, t2, True)}')
