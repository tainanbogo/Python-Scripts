'''sexo = str(input("Digite seu sexo: [M/F] ")).upper()
while sexo != str:
    if sexo == "M" or sexo == "F":
        print("Sexo {} registrado com sucesso!".format(sexo))
        break
    else:
        print("Dados inválidos. Por favor, digite novamente.")
        sexo = str(input("Digite seu sexo: [M/F]")).upper()'''

sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input("Dados Inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))


