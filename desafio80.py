lista = list()
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    #Se o número for o primeiro....
    if i == 0:
        lista.append(n)
        print(f'O valor {n} foi adicionado ao final da lista.')
    #... ou for maior que o último número
    elif n > lista[-1]:
        lista.append(n)
        print(f'O valor {n} foi adicionado ao final da lista.')
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'O valor {n} foi adicionado na posição {posicao} da lista.')
                break
            posicao += 1

print(f'Os valores digitados foram {lista}')
