import math
from random import random, sample, shuffle
from secrets import choice

#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
print('{:=^40}'.format(f'Apagar valor fracionário'))
num = float(input('Digite qualquer número real: '))
numint = math.trunc(num)
print(f'O valor desse número real sem seus decimais é: {numint}')
print('='*40)


n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))
hipo = math.hypot(n1,n2)
print(f'O comprimento da hipotenusa é de: {hipo:.2f}')


ang = int(input('\n\nDigite o ângulo: '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O cosseno do ângulo {ang} é de {cos:.2f} , o seno {sen:.2f} e a tangente {tan:.2f}.')


alu1 = input('\n\nDigite o nome do aluno 1 : ')
alu2 = input('Digite o nome do aluno 2 : ')
alu3 = input('Digite o nome do aluno 3 : ')
alu4 = input('Digite o nome do aluno 4 : ')
#lista = [alu1,alu2,alu3,alu4
#escolhido = random.choice(lista)
esc = choice([alu1,alu2,alu3,alu4]).capitalize()
print('O escolhido foi: ',esc)
#lista = [alu1,alu2,alu3,alu4]
#random.shuffle(lista)
print(f'Ordem de entrega de trabalho será:\n{sample([alu1,alu2,alu3,alu4], k=4)}')

