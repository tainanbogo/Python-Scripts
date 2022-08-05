from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print("+++ Suas Opções +++")
jogador = int(input("[0] Pedra\n"
            "[1] Papel\n"
            "[2] Tesoura\n"
            "Qual a sua jogada? "))
