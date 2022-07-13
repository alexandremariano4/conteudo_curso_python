import math
import random
print('{:=^40}'.format(f'Raiz quadrada'))
#num = float(input('Digite um número: '))
num = random.randint(1,50)
print(f'A raiz quadrada de {num} é {math.sqrt(num):.2f}.')
print('='*40)