cidade = str(input('Digite o nome da sua cidade: '))
cid = cidade.split()[0].capitalize()
santo = 'Santo' in cid
print(f'É verdade que o nome da cidade começa com "Santo"?: {santo}')
print(f'O nome da sua cidade começa com {cid}')