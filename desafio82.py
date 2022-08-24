lista = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    continuar = str(input('Quer continuar? [S/N]: '))
    if continuar.upper().strip()[0] in 'Nn':
        break
    else:
        if continuar.strip().upper()[0] not in 'Ss':
            print(f'Não entendi. Digite novamente.')
            continuar = str(input('Deseja continuar? [S/N]: '))
print(f'A lista completa de números é {lista}')
for c, i in enumerate(lista):
    if lista[c] % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
par.sort()
impar.sort()
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')

