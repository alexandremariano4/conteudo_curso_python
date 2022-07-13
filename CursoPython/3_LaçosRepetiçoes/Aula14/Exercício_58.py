from random import randint
numero = randint(1,10)
jogador = 0
tentativa = 1
while jogador != numero:
    print('-=-'*30)
    jogador = int(input('\033[1;34mTente adivinhar o número que eu pensei!\n\033[m'))
    if jogador != numero:
        tentativa = tentativa +1 
print(f'Você acertou!! O número que eu pensei é \033[1;33m{numero}\033[m!!!')
print(f'Você acertou em \033[1;35m{tentativa}\033[m tentativa(s) !!')
    