alunos = list()
cadastro = [" ", 0, 0, 0]
while True:
    cadastro[0] = str(input('Nome do aluno: '))
    cadastro[1] = float(input('Nota 1: '))
    cadastro[2] = float(input('Nota2: '))
    cadastro[3] = (cadastro[1] + cadastro[2])/2
    alunos.append(cadastro[:])
    continuar = str(input('Quer continuar? [S/N]:  '))
    if continuar in "Nn":
        break
print('=-' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for i, e in enumerate(alunos):
    print(f'{i:<4} {e[0]:<10}  {e[3]:>8.1f}')

while True:
    print("=-" * 30)
    ask = int(input('Quer mostrar as notas de qual aluno?'))
    if ask == 999:
        break
    if ask <= len(alunos) - 1:
        print(f'Notas de {alunos[ask][0]} são {alunos[ask][1]} e {alunos[ask][2]}')

