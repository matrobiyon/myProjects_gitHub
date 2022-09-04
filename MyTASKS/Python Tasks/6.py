#Ряд Фибоначчи
fib1 = 1 #1
fib2 = 1 #2
print(fib1)
print(fib2)
z = 0
while z <=5:
    fib3 = fib2 + fib1
    fib1 = fib2
    fib2 = fib3
    z += 1
    print(fib3, end="\n")

#Таблица умножения
for i in range(1,10):
    z = 1
    while z < 11:
        print("%.1d"%(i*z), end=" ")
        z += 1
        if (z == 11):
            print(end="\n")

#Дана формула: Найдите пошаговый ответ!
x = float(input("Начало отрезка: "))
intb = float(input("Конец отрезка: "))
shag = float(input("Chislo wagov: "))
while x < intb:
    y = -3*x**2 - 4*x + 20
    print("%5.2f" %x, end=" |")
    print("%7.2f" %y)
    x = x + shag




