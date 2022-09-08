lista = list()
pessoas = dict()
mulheres = list()
soma = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    lista.append(pessoas.copy())
    soma += pessoas['idade']
    media = soma/len(lista)
    if pessoas['sexo'] in 'Ff':
        mulheres.append(pessoas.copy())
    continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in "Nn":
        break
    if continuar not in "Ss":
        print('ERRO! Responda Sim ou Não')
        continuar = str(input("Quer continuar? [S/N]: "))
print('=-' * 30)
print(pessoas)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas')
print(f'B) A média de idade é de {media:5.2f}')
print('C) As mulheres cadastradas foram:')
for i in mulheres:
    print(f'{i}')
print(f'As pessoas com idade acima da média foram: ')
for p in lista:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v};', end='')
print()
print('ENCERRADO')

