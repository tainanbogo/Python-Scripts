jogador = dict()
gols = list()
contador = 0
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Qts partidas {jogador["nome"]} jogou?'))
jogador['gols'] = list()
for c in range(0, jogador['partidas']):
    contador = int(input(f'Quantos gols na partida {c}: '))
    total += contador
    gols.append(contador)
    jogador['gols'] = gols
    jogador['total'] = total
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, i in jogador.items():
    print(f'O campo {k} tem valor {i}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols.')
