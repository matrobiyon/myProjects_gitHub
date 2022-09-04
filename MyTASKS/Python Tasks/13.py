#Сколько элементов списка имеют значения больше чем у соседних элементов
from random import randint
a = []
for i in range(10):
    a.append(randint(1,100))
print(a)
num = 0
for i in range(len(a)):
    if a[i] == a[0] or a[i] == a[-1]:
        pass
    elif a[i-1] < a[i] > a[i+1]:
        print(a[i])
        num = num + 1
    else:
        pass
print(num)




