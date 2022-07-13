tupla = ('aprender','programar','linguagem','python','curso')

for v in tupla:
    print(f'\nNa palavra {v.upper()}, temos as vogais ',end='')
    for letra in v:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
       
