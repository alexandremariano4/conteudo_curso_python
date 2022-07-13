qtd = s = 0
print('{:-^60}'.format('Ler número e retornar quantidade e soma'))
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    qtd += 1
    s += n
print(f'Você inseriu {qtd} números, e a soma deles é de {s}!!!')