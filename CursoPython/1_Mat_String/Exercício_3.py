#Código que mostra o número antecessor e sucessor ao que digitou
n1 = int(input('Digite um número: '))
print(f'Número antecessor ao que você digitou: {n1-1}\nNúmero sucessor ao que você digitou: {n1+1}')

#ler o número, mostrar o dobro, triplo e raiz quadrada
n2 = int(input('\n\nDigite outro número: '))
print(f'O dobro do que você digitou: {n2*2}')
print(f'O triplo que você digitou: {n2*3}')
print(f'A raiz quadrada do que você digitou: {n2**(1/2):.2f}')

#Ler duas notas de e mostrar média
nota1 = float(input('\n\nDigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print(f'Média das notas: {media:.2f}')

#Programa que recebe o valor em metros e converta para  centimetros e milimetros e exiba
m = float(input('\n\nDigite o valor em metros: '))
print(f'Em centímetros: {m*100}')
print(f'Em milimetros: {m*1000}')

#Recebe um valor e exibe a tabuada desse valor
n3 = int(input('\n\nDigite um número de 1 a 10: '))

print('{:=^40}'.format(f'TABUADA do {n3}'))
print(f'1x{n3}={n3*1}')
print(f'2x{n3}={n3*2}')
print(f'3x{n3}={n3*3}')
print(f'4x{n3}={n3*4}')
print(f'5x{n3}={n3*5}')
print(f'6x{n3}={n3*6}')
print(f'7x{n3}={n3*7}')
print(f'8x{n3}={n3*8}')
print(f'9x{n3}={n3*9}')
print(f'10x{n3}={n3*10}')
print('='*40)

#Recebe o valor em real e retorna dólar
real = float(input('\n\nQuanto você tem de dinheiro em R$: '))
dolar = real*4.95
print(f'Você tem {dolar:.2f} dólares.')

#Fazer um programa que leia a largura e altura de uma parede em metros, calcule a sua área e quantidade de tinta necessária para pintá-la
#Sabendo que cada litro de tinta pinta uma área de 2m²
lar = float(input('\n\nDigite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = alt*lar
print(f'A parede tem {area}m².')
print(f'Para essa parede e levando em consideração que 1 Litro de tinta pinta uma área de 2m², será necessário {(1*area)/2} litros de tinta para pintar a parede de {area}m². ')

#Receber o preço do produto e dar 5% de desconto
produto = float(input('\n\nPreço do produto: '))
print(f'Preço com 5% de desconto: {produto*0.95}')

#Receber o salário e dar 15% de aumento
salario = float(input('\n\nQual seu salário: '))
print(f'Seu novo salário com 15% de aumento é de: {salario*1.15}!')