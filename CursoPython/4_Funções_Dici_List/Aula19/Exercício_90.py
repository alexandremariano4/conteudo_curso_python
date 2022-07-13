aluno = {}
######### PARA DICIONÁRIOS USAR .ITEMS() E PARA LISTAS ENUMARETE
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7.0:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print(f'O nome do aluno é {aluno["nome"]} sua média é {aluno["media"]} e sua situação é {aluno["situação"]}')