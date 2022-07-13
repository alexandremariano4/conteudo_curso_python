lista = list()
opcao = ''
while True:
    lista.append(int(input('Digite um número: ')))
    opcao = str(input('Deseja continuar: [S/N]: ')).strip().upper()[0]
    if 'N' in opcao:
        print('Fim do programa')
        break
    
print(f'Você digitou {len(lista)} elementos!')
print(f'Lista original: {lista}')
if 5 in lista:
    print(f'O valor 5 foi inserido na lista, na posição {lista.index(5)+1}')
else: 
    print('Não foi encontrado o número 5 na lista!')
lista.sort(reverse=True)
print(f'A lista inserida decrescente é: {lista}')
