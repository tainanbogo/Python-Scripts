matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor [{linha},{coluna}]: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()


