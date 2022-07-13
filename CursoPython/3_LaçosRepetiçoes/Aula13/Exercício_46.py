
from time import sleep

for c in range (10 , -1 , -1):
    sleep(1)
    print('\033[1;32m',c,'\033[m')
print('\033[1;31mKABOOOOM!!! \033[m')

