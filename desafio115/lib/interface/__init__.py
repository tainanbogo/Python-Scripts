def leiaint(msg):
   while True:
        try:
            a = int(input(f'{msg}'))
        except(ValueError, TypeError):
            print(f'\033[31mNúmero inválido. Por favor digite outro valor.\033[m')
            continue
        else:
            return a

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc
