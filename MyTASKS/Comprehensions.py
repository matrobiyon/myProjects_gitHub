from random import randint
list_ = []
def add1(i):
    return i+2
def isOdd(x):
    return x % 2 == 0

for i in range(1,11):
    list_.append(randint(1,100))

print(list_)

x = list(map(add1,filter(isOdd,list_)))
print(x)
