def misolho(a,b):
    misoli1 = a+b*a//2
    misoli2 = a-b*a%b
    misoli3 = a*b*a**2
    misoli4 = a/b*a**b
    print("Javobi misoli 1: " + str(misoli1))
    print("Javobi misoli 2: " + str(misoli2))
    print("Javobi misoli 3: " + str(misoli3))
    print("Javobi misoli 4: " + "%.2f"%(misoli4))

misolho(43,54)
misolho(7,9)
misolho(8,4)
misolho(3,5)


class misol():
    A = True
    while A:
        x = True
        ask_1 = input("Адади 1-умро ворид кунед: ")
        while x:
            if ask_1.isdigit():
                num_1 = int(ask_1)
                x = False
            else:
                ask_1 = input("Адади 1-умро ворид кунед: ")
                x = True
        y = True
        ask_2 = input("Адади 2-юмро ворид кунед: ")
        while y:
            if ask_2.isdigit():
                num_2 = int(ask_2)
                y = False
            else:
                ask_2 = input("Адади 2-юмро ворид кунед: ")
                y = True
        ask_q = input("Кадом амалро ба анчом расонданиед? +|-|*|/|")
        z = True
        #Танхо ададхои бебутун хисоб карда мешавад (INT), на ин ки FLOAT
        while z:
            if ask_q == "+":
                res_1 = num_1 + num_2
                print(str(num_1) + " " + ask_q + " " + str(num_2) + " баробар аст ба " + str(res_1))
                z = False
            elif ask_q =="-" and num_1 > num_2:
                res_2 = num_1 - num_2
                print(str(num_1) + " " + ask_q + " " + str(num_2) + " баробар аст ба " + str(res_2))
                z = False
            elif ask_q =="*":
                res_3 = num_1 * num_2
                print(str(num_1) + " " + ask_q + " " + str(num_2) + " баробар аст ба " + str(res_3))
                z = False
            elif ask_q =="/":
                res_4 = num_1 / num_2
                print(str(num_1) + " " + ask_q + " " + str(num_2) + " баробар аст ба " + str(res_4))
                z = False
            else:
                print("Хато! Бори дигар раками дурустро ворид кунед:  ")
                ask_q = input("Кадом амалро ба анчом расонданиед? +|-|*|/|")
                z = True

misol()




