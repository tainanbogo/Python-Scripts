print("Sequência de Fibonacci")
n = int(input("Quantos termos você quer mostrar? "))
t0 = 0
t1 = 1
print("{} -> {} -> ".format(t0, t1), end=" ")
cont = 3
while cont <= n:
    t2 = t0 + t1
    print("{} -> ".format(t2), end="")
    t0 = t1
    t1 = t2
    cont += 1
print("FIM!")