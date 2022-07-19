import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o seno de {:.2f}\nO cosseno de {:.2f}\nA Tangente de {:.2f}'.format(angulo, seno, cos, tangente))