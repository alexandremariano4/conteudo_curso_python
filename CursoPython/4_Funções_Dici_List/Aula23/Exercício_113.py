def VerifyInteger(num=0):
    res = num.isnumeric()
    if num == '':
        return(0)        
    while res != True:
        num = str(input(f'ERRO!! {num} não é um número inteiro, favor inserir um valor válido: '))
        res = num.isnumeric()
    if res == True:
        return int(num)


def VerifyReal(num=0):
    res = num.replace('.','').isnumeric()
    if num == '':
        return(0)
    while res != True:
        num = str(input(f'ERRO!! {num} não é um número real, favor inserir um valor válido: '))
        res = num.replace('.','').isnumeric()
    if res == True:
        return float(num)


try:  
    try:
        inteiro = str(input('Digite um número Inteiro: ')).strip()
        inteiro = VerifyInteger(inteiro)
        real = str(input('Digite um número Real: ')).strip().replace(',','.')
        real = VerifyReal(real)
    except (KeyboardInterrupt):
        print(f'\nUsuário encerrou o sistema!!!')
    except Exception as error:
        print(f'Ocorreu um erro! {error}')
    print(f'Você digitou os números {inteiro} e {real}. ')
except NameError:
    pass
finally:
    print('Volte sempre!')