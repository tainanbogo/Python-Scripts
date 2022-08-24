primeirotermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
c = 1
mais = 10
total = 0
print(primeirotermo, "->", end=" ")
while mais != 0:
    total = total + mais
    while c <= total:
        primeirotermo = primeirotermo + razao
        c += 1
        print(primeirotermo, "-> ", end=" ")
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Acabou")