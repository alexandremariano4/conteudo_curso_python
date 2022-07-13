valores = [9,2,6,0,1,5,14,21]

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos += 1

print(valores)
dobra(valores)
print(valores)
