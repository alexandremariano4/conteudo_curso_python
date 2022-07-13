from time import sleep

def contador(i,f,p):
    print(f'Contagem de {i} até o {f} de {p} em {p}')
    if p < 0:
        p = p * -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='',flush=True)
            sleep(0.5)
            cont += p
        print('Fim')
        print('-='*20)
    else:
        cont = i 
        while cont >= f:
            print(f'{cont} ',end='',flush=True)
            cont -= p
        print('Fim')
        print('-='*20)

     
contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('INÍCIO: '))
fim = int(input('FIM: '))
pas = int(input('PASSO: '))
contador(ini,fim,pas)
