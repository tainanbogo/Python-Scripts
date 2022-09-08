time = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partida = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for n in range(0, partida):
        gols.append(int(input(f'Qts gols na partida {n}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
    if resp not in 'Ss':
        print('ERRO. Digite Sim ou não')
        resp = str(input('Quer continuar? [S/N]'))
print('=-' * 30)
print(f"{'Cód/Nome':<15} {'Gols':^9} {'Total':>10}")
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} {v["nome"]:<10} {v["gols"]} {v["total"]:<8}')
while True:
    busca = int(input("Quer ver os dados de qual jogador? [999 para parar]"))
    if busca == 999:
        break
    if busca >= len(time):
       print(f'Não existe jogador com o código {busca}')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'No jogo {i+1} fez {g} gols.')
        print('=-' * 30)



