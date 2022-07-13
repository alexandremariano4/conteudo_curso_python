def linha():
    return '-' * 42

def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())
    
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    cont = 1
    for c in lista:
        print(f'{cor["yellow"]}{cont}{cor["clear"]} - {cor["blue"]}{c}{cor["clear"]}')
        cont += 1
    linha()
    opc = leiaInt('Sua opção: ')
    return opc
    
def leiaInt(msg):
    while True:
        try: 
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
        
    

cor = {
    'clear': '\033[m',
    'red': '\033[31m',
    'green': '\033[32m',
    'blue': '\033[34m',
    'yellow': '\033[33m'
}