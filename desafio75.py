num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor nove apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 está na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi encontrado.')
print('Os valores digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n}, ', end=' ')

# Minha Solução
'''nove = 0
tres = 0
pares = 0
for c in range(0, len(num)):
    if num[c] == 9:
        nove += 1
    if num[c] == 3:
        tres = c
    if num[c] % 2 == 0:
        pares += 1
print(f'Você digitou os valores {num}.\n '
      f'O valor 9 apareceu {nove} vezes.\n '
      f'O valor 3 apareceu na {tres + 1}ª posição.\n'
      f'O valores pares digitados foram {pares} ')'''


