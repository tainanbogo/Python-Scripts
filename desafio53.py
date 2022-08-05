frase = str(input("Digite uma frase: ")).upper().replace(" ","")
inverso = ''
for c in range(len(frase) - 1, - 1, -1):
    inverso = inverso + frase[c]

print(frase, inverso)

if inverso == frase:
    print('Essa frase é um palindromo')
else:
    print("Essa frase não é um palindromo")





