vel = float(input('Qual a velocidade atual do carro? '))
if vel <= 80:
    print('Sua velocidade é de {}. Tenha um bom dia! Dirija com segurança'. format(vel))
else:
    multa = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite de 80km/h!\n Você deve pagar uma multa de R${}'.format(multa))
