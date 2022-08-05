from random import randint
numero = randint(0,10)
print("Sou seu computador e acabei de pensar em um número de 0 a 10! \n"
      "Será que você consegue adivinhar?")
palpite = int(input("Digite seu palpite: "))
tentativa = 0
while palpite != numero:
    if palpite < numero:
        print("Mais... Tente novamente!")
        palpite = int(input("Digite seu palpite: "))
        tentativa += 1
    else:
        print("Menos... Tente novamente!")
        palpite = int(input("Digite seu palpite: "))
        tentativa += 1
print("Acertou com {} tentativas! Parabéns!".format(tentativa+1))

'''Outra opção
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual seu palpite?'))
    palpite += 1
    if jogador == computador:
        print(Acertou)
    else:
        if jogador < computador:
            print("Mais...Tente Novamente")
        elif jogador > computador: 
            print("Menos...Tente Novamente")
print("Acertou com {} tentativas".format(palpite))'''


