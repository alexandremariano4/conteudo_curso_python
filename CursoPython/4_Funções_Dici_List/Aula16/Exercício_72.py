numeros = ('Zero','Um','Dois','Tres','Quatro','Cinco',
           'Seis','Sete','Oito','Nove','Dez','Onde',
           'Doze','Treze','Quatorze','Quinze','Dezesseis',
           'Dezessete','Dezoito','Dezenove','Vinte')

opcao = int(input('Digite um número entre 0 e 20: '))
if opcao > 20 or opcao < 0:
    while opcao > 20 or opcao <0:
        opcao = int(input('Valor inválido, insira um valor entre 0 e 20: '))
print(f'Você digitou o número {numeros[opcao]}')