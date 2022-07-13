from datetime import date

def voto(idade):
    if idade < 16:
        print(f'Com {idade} anos: NÃO PODE VOTAR')
    elif idade < 65 and idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade >= 16 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')


print('-='*20)
anoNasc = int(input('Em que ano você nasceu: '))
idade =  date.today().year - anoNasc
voto(idade)
