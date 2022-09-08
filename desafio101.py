from datetime import datetime
def voto(ano=0):
    ano = int(input(f'Em que ano você nasceu?'))
    idade = datetime.now().year - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')
    elif idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')

voto()

