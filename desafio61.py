primeirotermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
c = 1
print(primeirotermo, "->", end=" ")
while c < 10:
    primeirotermo = primeirotermo + razao
    c += 1
    print(primeirotermo, "-> ", end=" ")
print("Acabou")
