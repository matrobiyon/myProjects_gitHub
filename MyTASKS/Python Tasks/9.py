from random import randint
#Найти минимальный по модуле элемент списка. Вывести его индекс и значение.
list = []
for i in range(0,10):
    list.append(randint(-50,50))
print(list)

num = 0
for b in range(0,10):
    if abs(list[b]) < abs(list[num]):
        num = b
print(abs(list[num]))


#Пороговое значение!
List = []
for i in range(10):
    List.append(randint(1,100))

ask = int(input("Porog: "))
newList = []
for i in range(10):
    if List[i] < ask:
        newList.append(List[i])
        List[i] = ask
print(newList)
print(List)








