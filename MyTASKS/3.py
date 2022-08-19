def misol():
    x = True
    ask_1 = input("Please add 1 number: ")
    while x:
        if ask_1.isdigit():
            num_1 = int(ask_1)
            x = False
        else:
            ask_1 = input("Please add 1 number: ")
            x = True
    y = True
    ask_2 = input("Please add 2 number: ")
    while y:
        if ask_2.isdigit():
            num_2 = int(ask_2)
            y = False
        else:
            ask_2 = input("Please add 2 number: ")
            y = True
    ask_q = input("What would you like to do?+|-|*|/|")
    z = True
    while z:
        if ask_q == "+":
            res_1 = num_1 + num_2
            print(str(num_1) + " " + ask_q + " " + str(num_2) + " is " + str(res_1))
            z = False
        elif ask_q =="-" and num_1 > num_2:
            res_2 = num_1 - num_2
            print(str(num_1) + " " + ask_q + " " + str(num_2) + " is " + str(res_2))
            z = False
        elif ask_q =="*":
            res_3 = num_1 * num_2
            print(str(num_1) + " " + ask_q + " " + str(num_2) + " is " + str(res_3))
            z = False
        elif ask_q =="/":
            res_4 = num_1 / num_2
            print(str(num_1) + " " + ask_q + " " + str(num_2) + " is " + str(res_4))
            z = False
        else:
            print("Wrong! Please add correct symbol! ")
            ask_q = input("What would you like to do?+|-|*|/|")
            z = True
misol()
