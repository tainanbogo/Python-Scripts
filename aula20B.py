def sum(a, b):
    soma = a + b
    print(soma)

sum(7, 3)
'''Para mudar a ordem dos parametros é necessário explicitar
Por exemplo: sum(b=7, a=3)'''

def soma(a, b):
    print(f'A soma de A = {a} + B = {b} é:')
    s = a + b
    print(f'{s}')

soma(b=4, a=5)

# Empacotando função

def contador(*num):
    for v in num:
        print(v)
    tamanho = len(num)
    print(len(num))

contador(2, 3, 4)
contador(6, 5)

# Inserindo listas em uma função
def dobra(lst):
    cont = 0
    while cont < len(lst):
        lst[cont] *= 2
        cont += 1


valores = [0, 2, 6, 3]
dobra(valores)
print(valores)

