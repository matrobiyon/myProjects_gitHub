from random import randint

List = []
for i in range(10):
    List.append(randint(1, 100))
print(List)
num1, num2 = 0, 0
for i in range(len(List)):
    if List[i] > List[num1]:
        num1 = i
for i in range(len(List)):
    if List[num2] < List[i] < List[num1]:
        num2 = i
print(List[num1], List[num2])

#Или же сначала отсортировать, потом выбрать -1 и -2
b = sorted(List)
print(b[-1])
print(b[-2])
