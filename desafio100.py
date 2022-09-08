from random import  randint
num = list()
def sortear(lista):
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[i]}', end=' ')

def somaPar(lista):
    soma = 0
    for e in lista:
        if e % 2 == 0:
            soma += e
    print(f'Somando os valores pares de {lista}, temos {soma}')


sortear(num)
print()
somaPar(num)

