''' Dicionário -> Declarando dicionário.
Aqui não trabalhamos com índices númericos, apenas com chaves nomeadas
que podem ser números ou palavras '''


pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22}
print(pessoas)
# Imprimindo apenas um elemento
print(pessoas['nome'])

# Declarando dentro de uma frase -> necessário usar aspas duplas
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

# Declarando apenas as chaves ou apenas os valores
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

# Acessando itens e chaves através de laços
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k} = {v}')

# Adicionando novo elemento
pessoas['estadocivil'] = 'solteiro'

print(pessoas)

# Apagando elementos
del pessoas['estadocivil']

print(pessoas)

# Modificando valor de elemento
pessoas['nome'] = 'Leandro'

print(pessoas)

# Criando dicionário dentro de lista
brasil = []
estado1 = {'UF': 'RJ'}
estado2 = {'UF': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

