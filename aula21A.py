# Utilizando o comando help e docstrings

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela:
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do Canal Curso em Video.
    """
    c = i
    while c <= f:
        print(f'{c}', end=" ")
        c += p
    print('FIM!')

help(contador)