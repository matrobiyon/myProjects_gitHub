#Сумма между максимальным и минимимальным числами!
from random import randint
spisok = []
for i in range(0,10):
    spisok.append(randint(1,50))
print(spisok)

# num1 = 0
# num2 = 100
# for i in spisok:
#     if i > num1:
#         num1 = i
#     if i < num2:
#         num2 = i
# print(num1,num2)

num1 = 0
num2 = 0
for i in range(0,10):
    if spisok[i] > spisok[num1]:
        num1 = i
    elif spisok[i] < spisok[num1]:
        num2 = 0
print(num1,num2)
