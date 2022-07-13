from unicodedata import numeric

#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.



n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
print(f"A soma entre {n1} e {n2} vale: {soma}!")

print('-----------------------------------------------')
n3 = input('Digite qualquer coisa: ')
print('O que você digitou é do tipo:',type(n3))
print(f'O que você digitou faz parte do alfabeto?:',n3.isalpha())
print(f'O que você digitou é numérico?:',n3.isnumeric())
print('O que você digitou só tem espaços?:',n3.isspace())
print('O que você digitou é alfa numérico?:',n3.isalnum())
print('O que você digitou está em maiúsculo?:',n3.isupper())
print('O que você digitou está em minúsculo?:',n3.islower())
print('O que você digitou está com a primeira letra em maiúsculo?:',n3.istitle())


print('-----------------------------------------------')




