# Вывести число обароное веднёному по порядку состовляющих его цифр. Например, введено 4324б, результат будет 64234
def masala(a):
    n2 = []
    text = str(a)
    hisob = 0
    a = True
    while a:
        for i in text:
            n2.append(i)
            hisob += 1
        a = False
    tup3 = tuple(n2)
    z = 0
    new_num = []
    while (z < hisob):
        z += 1
        new_num.append(tup3[-z])
    new_num_str="".join(new_num)
    print(new_num_str)

masala(7542)

#2 sposob kak na knige
n1 = int(input("Chislo:"))
n2 = 0
while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 +digit

print("Obratno: " + str(n2))

print(245 // 10)

#Самая сложныя задача в данном время!!
#Самая сложныя задача в данном время!!
#Самая сложныя задача в данном время!! 