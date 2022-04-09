zna=input('''Орел или Решка?
Введите О или Р  ''')
znach=''
if zna=='О':
    znach='Орел'
elif zna=='Р':
    znach='Решка'
import random
zz=['Орел', 'Решка']
g=(random.choice(zz))
if znach==g:
    print(g)
    print('Совпадение')
else:
    print(g)
    print('Несовпадение')