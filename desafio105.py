def notas(*num, sit=False):
    '''
    -> Permite a análise das notas de um aluno
    :param num: Notas (sem limite)
    :param sit: situação do aluno em relação a média da turma
    :return: Dicionário com total de notas, maior e menor nota e situação.
    '''
    n = list()
    for e in num:
        n.append(e)
    n.sort()
    ficha = {
        'total': len(n),
        'maior': n[-1],
        'menor': n[0],
        'média': sum(n)/len(n)
    }
    if sit == True:
        if ficha['média'] < 5:
            ficha['situação'] = 'RUIM'
        if ficha['média'] <= 7:
            ficha['situação'] = 'MEDIANO'
        if ficha['média'] <= 10:
            ficha['situação'] = 'EXCELENTE'
    print(ficha)

notas(5, 6, 8, 10, sit=True)
notas(8, 10, 5)


