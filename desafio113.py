def leiaint(msg):
   while True:
        try:
            a = int(input(f'{msg}'))
        except(ValueError, TypeError):
            print('Número inválido. Por favor digite outro valor.')
            continue
        else:
            return a

def leiafloat(msg):
   while True:
        try:
            b = float(input(f'{msg}'))
        except(ValueError, TypeError):
            print('Número inválido. Por favor digite outro valor.')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            break
        else:
            return b

a = leiaint('Digite um número: ')
b = leiafloat('Digite outro número: ')
c = a / b
print(f'A divisão de {a} por {b} é igual a {c}')












