palavras = ('APRENDER', 'PROGRAMAR',
            'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for v in p:
        if v.lower() in 'aeiou':
            print(f'{v}', end=' ')
