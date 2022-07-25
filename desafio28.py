import random

print('Vou pensar em um número entre 0 e 5. Tente Adivinhar!')
x = random.randint(0,5)
chute = int(input('Em que número eu pensei? '))
if chute == x:
    print('Parabéns! Eu pensei exatamente no número {}'.format(x))
else:
    print('Que pena, eu pensei no número {}.Tente novamente!'.format(x))


