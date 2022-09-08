def ficha(jog="<desconhecido>", gols=0):
    print(f'O jogaddor {jog} fez {gols} gols(s) no campeonato')
nome = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)
