from time import sleep

from lib.interface import *
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRADO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema....Até Logo')
        break
    else:
        cabeçalho('ERROR! Digite um número válido.')
    sleep(1)
