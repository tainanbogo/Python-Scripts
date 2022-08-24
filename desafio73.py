time = ('Corinthians', 'Palmeiras', 'Santos',
        'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
        'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR',
        'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Times do Brasileirão: {time}')
print('=-' * 20)
print(f'Os 5 primeiros são: {time[0:5]}')
print('=-' * 20)
print(f'Os quatro últimos são: {time[-4:]}')
print('=-' * 20)
print(f'Os times em ordem alfabética são {sorted(time)}')
print('=-' * 20)
print(f'O Chapecoense está na {time.index("Chapecoense") + 1}ª posição')