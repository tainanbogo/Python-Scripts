n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2

if media >= 7:
    print("Sua média foi {:.1f}. Você está APROVADO!".format(media))
elif media >=5:
    print("Sua média foi {:.1f}. Você está de RECUPERAÇÃO!".format(media))
else:
    print("Sua média foi {:.1f}. Você está REPROVADO!".format(media))
