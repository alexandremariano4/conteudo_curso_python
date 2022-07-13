def notas(lista,sit=True):

    s = 0
    for num in lista:
        s = s+num
    dic = {'maior': max(lista),
        'menor': min(lista),
        'média': (s/len(lista))}
    if sit == True:
        if dic['média'] > 6:
            dic['situacao'] = 'APROVADO'
        if dic['média'] < 6:
            dic['situacao'] = 'REPROVADO'
        print(dic)
    else: 
        print(dic)
    
situ = {'S': True, 'N': False}

TotNotas = []

qtdNotas = int(input('Quantas notas deseja inserir: '))
for cont in range(0,qtdNotas):
    nota = float(input(f'Nota {cont+1}: '))
    TotNotas.append(nota)
sit = str(input('Deseja visualizar também a situação do aluno? [S/N] ')).upper().strip()[0]
notas(TotNotas,situ[sit])