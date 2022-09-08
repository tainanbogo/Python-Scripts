# Escopo de variaveis
''' Dependendo de onde a variavel for declarada ela
somente valerá dentro da função
ou será global, ou seja, valerá no programa inteiro. '''

def funcao():
    n1 = 2
    print(f'N1 dentro vale {n1}')

n1 = 4
print(f'N1 fora vale {n1}')
funcao()

''' Caso eu quisesse impedir a criação de uma variavel n1 dentro da função
seria necessário apenas declarar dentro da função, global n1, ou seja, 
utilize a variavel n1 global e não crie outra com essa denominação.'''
