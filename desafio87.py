matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = coluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Número [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if matriz[l][2]:
            coluna += matriz[l][2]
        if matriz[1][c] > maior:
            maior = matriz[1][c]



print(matriz)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores terceira coluna é {coluna}')
print(f'O maior número da terceira linha é {maior}')

