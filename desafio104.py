def leiaint(frase):
    while True:
        v = input(frase)
        if v.isnumeric():
           return v
        else:
            print('\033[0;31mERRO! Digite um número válido\033[m')

n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
