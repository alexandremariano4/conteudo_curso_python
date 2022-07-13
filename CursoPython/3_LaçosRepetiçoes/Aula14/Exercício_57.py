sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [F/M]: ')).upper().strip()
    if sexo != 'm' and sexo != 'f':
        print('Digite um valor válido [S/N]')
        
print('Fim do programa, seu sexo é {}'.format(sexo))
    
    