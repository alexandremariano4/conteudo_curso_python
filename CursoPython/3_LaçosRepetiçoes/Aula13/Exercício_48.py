from time import sleep

soma = 0
cont = 0 
for c in range (1, 500+1):
    if c % 3 == 0:
        print(c)
        soma = soma + c
        cont = cont + 1
print(soma)
print(cont)
