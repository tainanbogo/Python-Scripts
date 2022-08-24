"""numero = [2, 4, 6, 8]
soma = 0

for i in numero:
    soma += i
media = soma/len(numero)
print(media)"""

lista = list()
for i in range (0,4):
    n = int(input('Digite um valor: '))
    if i == 0:
        lista.append(n)
        print(f'O número {n} foi adicionado ao final da lista')
    elif n > lista[-1]:
        lista.append(n)
        print(f'O número {n} foi adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'O valor {n} foi adicionado a posição {posicao}')
                break
            posicao += 1

print(f'Os valores digitados foram {lista}')










