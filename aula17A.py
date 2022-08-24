# Declarar uma lista
num = [2, 5, 9, 1]   # ou num = list()
print(num)
# Modificar um elemento da lista
num[2] = 3
print(num)
# Adicionar um novo elemento -> Aqui adiciona-se apenas ao final.
num.append(7)
print(num)
# Outra maneira de adicionar outro elemento -> Dessa maneira é possivel adicionar em qualquer posição
num.insert(0, 0)
print(num)
# Classificar a lista em ordem
num.sort()
print(num)
# Classificar em ordem inversa
num.sort(reverse=True)
print(num)
# Eliminar um elemento
num.pop() #assim elimina o elemento final
print(num)
# Eliminar o elemento de qualquer posição
num.pop(1)
print(num)
# Buscar valor e elimina o primeiro que achar -> ELIMINA O VALOR, não a posição
num.remove(3)  # Caso exista um valor repetido ele elimina apenas o primeiro que encontrar
print(num)  # Se ele não encontrar o valor dá erro
# Para buscar elemento e elimina-lo
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')


# Outra maneira de adicionar valores
valores = []
for cont in range(6, 10):  # No range pode colocar o intervalo que quiser.
    valores.append(cont)
for c, cont in enumerate(valores):
    print(f'Na posição {c} encontrei o  valor {cont}')
print(f'Cheguei ao final da lista')

# Copiando listas
# Criando lista A
a = [2, 3, 4, 7]
print(a)
# Criando Lista B
b = a
print(b)
# Modificando elemento na lista B
b[2] = 8
# Será que modificou ambas ou apenas a B?
print(a, b)
# Se vc cria uma lista igual a outra você não faz uma cópia da lista.
# Caso mude algo em uma lista, a outra também será modificada
# Para criar uma cópia é necessário declarar:
c = a[:]
print(c)
c[2] = 3
print(c, a)
