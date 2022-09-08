# Listas Compostas
# Declarando lista
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

# Copiando lista
galera = list()
galera.append(teste)
print(galera)

# Modificando Lista
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(teste)
print(galera)

''' Para que os elementos da lista composta sejam atualizados é necessário
fazer uma cópia da lista original, assim os elementos serão atualizados e não apeas repetidos'''

# Fazendo cópia da lista
galera.append(teste[:])  # fazer isso inicialmente após cada modificação de lista

# declarando uma lista composta do zero

galere = [['Maria', 22], ['Gustavo', 25], ['André', 18], ['Joaquim', 23]]
print(galere)
print(galere[2][1])

for p in galere:
    print(f'{p[0]} tem {p[1]} anos de idade')

# Pedindo para o usuario declarar a lista
pessoas = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)

# Fazendo condicionais dentro da lista
for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} tem {p[1]} anos de idade. MAIOR')
    else:
        print(f'{p[0]} tem {p[1]} anos de idade. MENOR')
