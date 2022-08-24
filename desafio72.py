num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    numero = int(input('Digite um número entre 0 e 10: '))
    if numero > 10 or numero < 0:
        print('Tente novamente.')
    else:
        print(f'Voce digitou o número {num[numero]}')
print('Obrigado e até a próxima!')
