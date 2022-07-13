import string

texto = str(input('Qualquer coisa: ')).strip().upper()
string = texto[::-1]

print('A palavra invertida fica: ''\033[1;31m',''.join(string.split()),'\033[m', '\nA palavra que você digitou é: ','\033[1;32m',''.join(texto.split()),'\033[m')

if ''.join(texto.split()) == ''.join(string.split()):
    print('A palavra informada é um palíndromo.')
else: 
    print('A palavra informada não é um palíndromo')
