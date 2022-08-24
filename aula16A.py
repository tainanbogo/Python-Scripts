# Tuplas são IMUTAVEIS, definidas por parenteses e aceitam diferentes elementos como numeros e strings

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[-1])
print(lanche[1:3])
print(lanche[-2:])
for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi demais!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi demais')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(d)
print(c.count(5))
print(c.index(8))
