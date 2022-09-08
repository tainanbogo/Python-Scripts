import time

def contador(c, m, p):
    print(f'-=' * 20)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if c < m:
        print(f'Contagem de {c} até {m} de {p} em {p}')
        for i in range(c, m+1, p):
            print(f'{i}', end=' ')
            time.sleep(0.5)
        print('FIM!')

    if m < c:
        print(f'Contagem de {c} até {m} de {p} em {p}')
        for i in range(c, m + 1, -p):
            print(f'{i}', end=' ')
            time.sleep(0.5)
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)

