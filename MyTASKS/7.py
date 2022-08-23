#Дано ряд чисел 1, -0.5, 0.25 -0.125 ... Найти их сумму если продолжить его n раз
inpNum = int(input("Skolko raz: "))
numb = 2
sum = 0
for i in range(1,inpNum+1):
    x = float(numb / 2)
    print(x)
    numb = -x
    sum = sum + x
print(sum)

#Являеться ли число простым
doxil = int(input("Raqamro doxil kuned: "))
if doxil > 0:
    if doxil % 2 == 0:
        print("Raqam oddi nest")
    else:
        print("Raqam oddi ast: ")

