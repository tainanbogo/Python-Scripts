valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[0]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor foi {menor} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'...{i}', end='')

# Minha resolução
'''lista = list()
maior = menor = 0
for c in range(0, 5):
    n = int(input(f'Valor para posição {c}: '))
    lista.append(n)
    if c == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(lista)
print(f'O maior valor foi {maior} na posição ', end='')
for i, v in enumerate(lista):
 if v == maior:
    print(f'{i}...', end=' ')
print()
print(f'O menor valor foi {menor} na posição ', end='')
for i, v in enumerate(lista):
 if v == menor:
    print(f'{i}...', end=' ')'''
