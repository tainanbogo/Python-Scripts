aluno = {
    'nome': str(input('Nome: ')),
    'media': float(input(f'Média: ')),
    'situação': " "}

if aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
elif aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
elif aluno['media'] <= 10:
    aluno['situação'] = 'Aprovado'

for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
