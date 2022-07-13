def maior(*num):
    for c in num:
        print(f'{c}',end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        print('O maior valor informado foi 0')
    else:
        print(f'O maior valor informado foi {max(num)}')
    print('-='*30)


maior(2,9,4,5,7,15,5,6,4,5,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()