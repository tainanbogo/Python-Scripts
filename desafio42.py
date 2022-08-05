print("-- Analisando Triângulos! --")
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (a + b > c) and (b + c > a) and (c + a > b):
    print('Estas medidas podem formar um Triângulo!')
    if a == b == c:
        print('Triangulo Equilátero!')
    elif (a == b != c) or (c == b != a) or (a == c != b):
        print('Triangulo Isósceles')
    else:
        print('Triangulo Escaleno')

else: print('Essas medidas não foram um triângulo! Tente Novamente!')