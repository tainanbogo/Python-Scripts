distancia = float(input('Qual a distância percorrida em KM? '))
dias = float(input('Agora informe a quantidade de dias: '))
vdistancia = distancia * 0.15
vdias = dias * 60
valor = vdistancia + vdias
print('Sua viagem de {} dias e {}Km sairá por: {}'.format(distancia, dias, valor))

