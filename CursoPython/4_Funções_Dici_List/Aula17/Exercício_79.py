lista = list()
while True:
    numero = int(input('Digite um valor: ')) 
    if numero in lista:
        while numero in lista:
            numero = int(input('Valor existente, digite outro valor: '))
            if numero not in lista:
                lista.append(numero)
                break 
    else:
        lista.append(numero)
        print('Valor adicionado com sucesso!')  
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao not in 'SN':
        while opcao  not in 'SN':
            opcao = str(input('Digite uma opção válida [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
lista.sort()
print(lista)