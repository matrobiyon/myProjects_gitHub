#Randomly choosing number beetween 0.1 and 0,5 with rounding it by 2 numbers after comma
from random import random, randint
x = randint(0,1)
y = random()*0.4+0.1
print(round(y,2))
print('%.2f'%y)

#random number with 3 numbers
rand_num = randint(100,999)
last_num = rand_num % 10
first_num = rand_num//100
second_num_1 = rand_num % 100
second_num_2 = second_num_1 // 10
sum = last_num + first_num + second_num_2
print(rand_num)
print(first_num, second_num_2,last_num)

print(sum)

#Даны два ненулевых числа. Найти сумму, разность, произведение и  частное их квадратов
def misol(a,b):
    sum = a**2+b**2
    raz = a**2-b**2
    proz = (a**2)*(b**2)
    chastnoe = (a**2)/(b**2)
    print('Summa: ' + str(sum),'\nRaznost: ' + str(raz) +'\nProizvedenie: '+str(proz)+'\nChastnoe: '+str(chastnoe))

misol(43,32)



