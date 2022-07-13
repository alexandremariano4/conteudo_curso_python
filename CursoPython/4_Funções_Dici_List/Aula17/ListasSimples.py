#list.append('') insere o valor no final da lista
#list.insert(0,'') insere o valor na posição inserida
#del.list[3] apaga o item exato dentro da lista
#list.pop(3) apaga o item exato dentro da lista
#list.pop apaga o último item da lista
#list.remove('') valor da lista
#valores = list(range(4,11)) => 4 5 6 7 8 9 10 nas posições 0,1,2,3,4,5,6
#-----------------
num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
# num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')
