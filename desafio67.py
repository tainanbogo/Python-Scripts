'''n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    c = 0
    if n < 0:
        break
    else:
        while c <= 10:
          print(f' {n} x {c} = {n * c}')
          c += 1
print('Programa Encerrado. Volte Sempre')'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} x {c} = {n * c}')
print('Programa Encerrado. Volte Sempre')