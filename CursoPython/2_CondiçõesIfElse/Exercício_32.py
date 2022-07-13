n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um  número: '))
n3 = int(input('Digite outro número: '))

if n1>n2 and n1>n3:
    print(f'O número {n1} é maior que {n2} e {n3}!')
elif n2>n1 and n2>n3:
    print(f'O número {n2} é maior que {n1} e {n3}!')
else:
    print(f'O número {n3} é maior que {n1} e {n2}')   
if n1<n2 and n1<n3:
    print(f'O número {n1} é menor que {n2} e {n3}!')
elif n2<n1 and n2<n3:
    print(f'O número {n2} é menor que {n1} e {n3}!')
else:
    print(f'O número {n3} é menor que {n1} e {n2}!')
    