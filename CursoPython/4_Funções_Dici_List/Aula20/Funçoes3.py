def soma (*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} é igual a {s}')
    
soma(5,4,8,6)
soma(0,2,4,6,2)
