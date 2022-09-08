def area():
    print(f'=-' * 15)
    print(f'    Controle  de Terreno  ')
    c = float(input('Digite o comprimento do terreno: '))
    l = float(input('Digite a largura do terreno: '))
    calc = c * l
    print(f'A área do terreno é {calc}m²')

area()
