# Return
'''Quando desejamos apenas informar o valor de uma função não é necessário
utilizar o print podemos apenas declarar o que queremos retornar ao programa
com isso utilizamos a palavra return a após escrevemos uma variavél.'''

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(2, 3, 4)
r2 = somar(3, 4)
r3 = somar(3)

print(f'Os resultados foram {r1}, {r2}, {r3}')
