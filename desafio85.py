numeros = list()
lista = list()
for c in range(0, 3):
    lista.append(int(input(f'Número {c}: ')))
    numeros.append(lista[:])
    lista.clear()
numeros.sort()
print(f'Os números pares digitados foram: ', end='')
for n in numeros:
    if n[0] % 2 == 0:
        print(f'{n}', end='')
print()
print(f'Os números ímpares digitados foram: ', end='')
for n in numeros:
    if n[0] % 2 == 1:
        print(f'{n}', end='')


