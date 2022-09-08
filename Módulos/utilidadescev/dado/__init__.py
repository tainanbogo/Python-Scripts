def leiadinheiro(msg):
    valido = False
    while not valido:
        n = str(input(f'{msg}')).replace(',', '.').strip()
        if n.isalpha() or n == "":
            print(f'\033[0;31mERRO! {n} não é um preço válido!\033[m')
        else:
            valido = True
            return float(n)
