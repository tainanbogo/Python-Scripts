print('Analisador de Triângulos')
print('-=' * 20)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print('As medidas {}, {}, {} podem formar um triângulo!'.format(a,b,c))
else:
    print('As medidas {}, {}, {} não podem formar um triângulo.'.format(a,b,c))