media = numero = qtd = 0
while numero != 1:
    
    if qtd == 0:
        print('Digite 1 para finalizar o programa')
    numero = int(input('Digite um número: '))
  
    if numero != 1:
        media = media + numero 
        qtd += 1
        
    
print(f'A média entre os números digitados é de {media/qtd:.2f}')
print(f'Foram digitados {qtd} números')