from random import randint
from time import sleep
from operator import itemgetter
jogador = dict()
jogador['jogador1'] = randint(1, 6)
jogador['jogador2'] = randint(1, 6)
jogador['jogador3'] = randint(1, 6)
jogador['jogador4'] = randint(1, 6)

ranking = list()

for k, v in jogador.items():
    print(f'{k} tirou {v}')
    sleep(1)

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

for k, v in enumerate(ranking):
    print(f'{k} lugar: ')







