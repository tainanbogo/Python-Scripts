# Argumentos opcionais
'''
A função abaixo tem 3 parametros, contudo caso seja esquecido de adicionar
algum, como por exemplo você informa a e b mas não informa c. Ao executa-lá
será retornado um erro. Para defini-la como argumento opcional vamos previamente
defini-la como 0, sendo assim ao invés de somar(a,b,c) teremos somar(a,b,c=0)
O mesmo pode ser feito com os outros parametros sem problema.
'''
def somar(a, b, c=0):
    """
    -> Faz a soma de 3 valores
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    Função criada por Gustavo Guanabara - CURSO EM VIDEO.
    """
    s=a+b+c
    print(f'A soma vale {s}')

somar(1, 2, 3)
somar(1,2)

