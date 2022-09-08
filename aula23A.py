# Tratamento de Erro

try:
    num = int(input('Numerador: '))
    div = int(input('Divisor: '))
    result = num / div
except Exception as erro:
    print(f'Infelizmente tivemos um problema :(. {erro.__class__}')
else:
    print(f'O resultado é {result:.1f}')
finally:
    print('Volte Sempre! Muito Obrigado!')
