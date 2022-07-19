import math
num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {} ou {:.0f} ou {}'.format(num, math.floor(num), num, math.trunc(num)))
