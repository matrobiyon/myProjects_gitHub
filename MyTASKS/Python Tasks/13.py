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
print(num)

count = 0
list_ = []
for z in range(10):
    list_.append(randint(1,100))
print(list_)
for i in range(1,len(list_)-1):
    if list_[i] > list_[i+1] and list_[i] > list_[i-1]:
        count +=1
print(count)




