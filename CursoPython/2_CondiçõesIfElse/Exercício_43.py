from time import sleep


peso = int(input('\033[1;34mPeso: \033[m'))
altura = float(input('\033[1;36mAltura: \033[m'))

imc = peso / (altura ** 2)

print('\033[1;33mPROCESSANDO IMC!!!!\033[m')
sleep(2)

if imc < 18.5:
    print(f'\033[1;32mSeu IMC é {imc:.1f} Você precisa comer mais!! Está abaixo do peso!\033[m')
elif imc >= 18.5 and imc < 25:
    print(f'\033[1;32mParabéns!!! Seu IMC é de {imc:.1f} mantenha sua alimentação boa! Você está com o peso ideal\033[m')
elif imc >= 25 and imc < 30:
    print(f'\033[1;31mTome cuidado!!! Você está com sobrepeso! Melhore sua alimentação e sua rotina de exercícios!!!\033[m')
elif imc >=30 and imc < 40:
    print(f'\033[1;31mSeu IMC é de {imc:.1f}, você está com obesidade GRAU 1 !!! Procure um médico nutricionista e melhore sua alimentação e exercícios físicos!\033[m')
else:
    print('Posso chamar o coveiro?')
    