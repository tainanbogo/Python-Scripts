from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))
sequencia = sorted(num)
print(f'Os números sorteados foram: {num}')
print(f'O menor número foi {sequencia[0]}'
      f' e o maior número foi {sequencia[4]}')

# Também podemos usar max(num) e min(num) para saber o maior e o menor

