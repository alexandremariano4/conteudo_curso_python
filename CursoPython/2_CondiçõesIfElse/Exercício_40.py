n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
n4 = float(input('Nota 4: '))

media = (n1 + n2 + n3 + n4) / 4 

if media < 5.0:
    print(f'\033[1;31mSua nota foi {media:.1f} Você foi reprovado!!!\033[m')
elif 6.9 > media >= 5:
    print(f'Sua nota foi {media:.1f} Você está de recuperação!!!')
else:
    print(f'\033[1;32mParabéns!!! Sua nota foi {media:.1f} Você foi aprovado!\033[m')
    