print('\033[1;34m-=-\033[m'*30)
r1 = float(input('\033[1mDigite o comprimento da reta 1: '))
print('\033[1;34m-=-\033[m'*30)
r2 = float(input('\033[1mDigite o comprimento da reta 2: '))
print('\033[1;34m-=-\033[m'*30)
r3 = float(input('\033[1mDigite o comprimento da reta 3: '))
print('\033[1;34m-=-\033[m'*30)

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    if r1 == r2 == r2 == r3:
        print('Esse é um triângulo EQUILÁTERO!!!!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse é um triângulo ISÓSCELES!!!')
    else:
        print('Esse é um triângulo ESCALENO!!!')
    print('\033[1;32mÉ possível montar um triângulo com essas retas!\033[m')
    

else:
    print('\033[1;31mNão poderá montar um triângulo com essas retas!\033[m')
