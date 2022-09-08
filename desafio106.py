c = ('\033[m',
     '\033[0,30,41m')
def line(msg, cor):
    tam = len(msg)
    print('*=' * tam)
    print(msg)
    print('*=' * tam)

def funbibli():
    while True:
        resp = str(input('Função ou Biblioteca: ')).strip().lower()
        if resp in 'fim':
            print('Até Logo!')
            break
        else:
            mostrar = help(resp)
            print(mostrar)


line()
funbibli()





