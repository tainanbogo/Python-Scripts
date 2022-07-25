distancia = float(input('Qual a distância da viagem? '))
preco1 = distancia * 0.5
preco2 = distancia * 0.45
if distancia <= 200:
    print('Sua viagem vai começar! Para viajar {}km sua passagem custará R${}'.format(distancia, preco1))
else:
    print('Sua viagem vai começar! Para viajar {}km sua passagem custará R${:.2f}'.format(distancia, preco2))
