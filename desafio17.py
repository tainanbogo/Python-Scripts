import math
cat0 = float(input('Comprimento do cateto oposto: '))
catA = float(input('Comprimento do cateto adjacente: '))
hip = math.sqrt((cat0 ** 2 + catA ** 2))
hip2 = math.hypot(cat0, catA)
print('A hipotenusa vai medir {:.2f} ou {:.2f}'.format(hip, hip2))
