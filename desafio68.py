from random import randint
v = 0
while True:
    n = int(input('Digite um valor: '))
    parImpar = input('Par ou impar [P/I]: ').upper().strip()[0]
    c = randint(0, 10)
    if (n + c) % 2 == 0 and parImpar == 'P':
        print(f'Você jogou {n} e o computador jogou {c}.Total de  {n + c}\n'
              f'Você escolheu PAR!\n'
              f'Você Venceu. Vamos Jogar Novamente!')
    elif (n + c) % 2 != 0 and parImpar == 'I':
        print(f'Você jogou {n} e o computador jogou {c}.Total de {n + c}\n'
              f'Você escolheu IMPAR!\n'
              f'Você Venceu. Vamos Jogar Novamente!')
    else:
        print(f'Você jogou {n} e o computador jogou {c}.\n'
              f'A soma dos valores é {n + c}\n'
              f'Você escolheu {parImpar}\n'
              f'GAME OVER!')
        break
    v += 1
print(f'Você venceu {v} vezes. Até a próxima!')
