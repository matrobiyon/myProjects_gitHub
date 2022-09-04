from random import randint
List = []
for i in range(10):
    List.append(randint(1, 100))
print(List)

sum = 0
for i in List:
    sum = sum + i

chislo = sum // len(List)
print(chislo)
for i in range(len(List)):
    if List[i] < chislo:
        del List[i]
        i = i - 1
    print(i)
print(List)
