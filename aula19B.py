estado = dict()
brasil = list()
# Criando elementos em Dicionário e adicionando a uma lista
for c in range(0, 3):
    estado['uf']= str(input('UF: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
# Imprimindo elementos da lista
for e in brasil:
    print(e)

# Imprimindo elementos da lista e dicionário personalizado

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
