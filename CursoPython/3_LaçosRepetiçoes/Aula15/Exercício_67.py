print('{:=^30}'.format('Tabuada'))
qtd = 0 

while True:
    print('='*30)
    n = int(input('Quer ver a tabuada de qual número: '))
    if n < 0:
        break  
    for c in range (1,11):
        print(f'{n} x {c} = {n*c}')
print('Programa encerrado!!!')