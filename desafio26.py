nome = str(input('Digite seu nome: ')).strip()
print('A letra A aparece {} vezes na frase.'.format(nome.upper().count('A')))
print('A primeira letra A aparece na posição {}'.format(nome.upper().find('A') + 1))
print('A última letra A aparece na posição {}'.format(nome.upper().rfind('A')))


