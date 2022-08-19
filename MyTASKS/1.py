import math
#My first task in Python. Good Luck for ME!

#Метод барои гирифтани INT аз USER бе хатоги!
def get_integer():
    x = True
    get_int_1 = input("Please add the 1-st kateter value: ")
    while x:
        if get_int_1.isdigit():
            print("OK")
            int_num_1 = int(get_int_1)
            x = False
        else:
            get_int_1 = input("Please add the 1-st kateter value: ")
            x = True
    y = True
    get_int_2 = input("Please add the 2-st kateter value: ")
    while y:
        if get_int_2.isdigit():
            print("OK")
            int_num_2 = int(get_int_2)
            y = False
            continue
        else:
            get_int_2 = input("Please add the 1-st kateter value: ")
            y = True
    return int_num_1, int_num_2

#Гирифтани INT аз DEF
num1, num2 = get_integer()

#Метод барои хисбкунии параметр ва масохати секунчаи росткунча
def sekunja(a,b):
    c = (b**2 + a**2)
    P = a + b + math.sqrt(c)
    S = 1/2 * a * b
    print("Perimetr equals to: " + str(P))
    print("Squad equals to: " + str(S))

sekunja(num1,num2)