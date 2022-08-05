from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
print("Quem nasceu no ano de {} tem {} anos de idade".format(nascimento, idade))

if idade == 18:
    print("Você deve ser alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print("Faltam {} anos para você se alistar.\n"
          "Seu alistamento será em {}".format(saldo, atual + saldo ))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos\n'
          'Seu alistamento foi em {}'.format(saldo, atual - saldo))

