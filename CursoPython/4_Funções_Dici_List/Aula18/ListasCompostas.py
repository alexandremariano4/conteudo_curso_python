teste = list()
teste.append('Alexandre')
teste.append(22)

galera = list()
galera.append(teste[:])

print(galera)
print('='*40)

teste[0] = 'Xumbim'
teste[1] = 24

galera.append(teste[:])
print(galera)
print('='*40)

pessoas = [['Abroba', 30],['Fresco', 22],['Bonobom', 10],['Graos', 15]]
print(pessoas[0][0])
print(pessoas[0])
print('='*40)

for pessoa in pessoas:
    # print('Nome:',pessoa[0],end=' → ')
    # print(pessoa[1])
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')