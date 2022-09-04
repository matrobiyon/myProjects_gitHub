#По введёным координатам точки определить в какой четверти оно находиться
#Так как в координате есть 4 четверти тогда
def koordina(a,b):
    if a > 0 and b >0:
        print("Koordinata naxodistya v 1 chetverti")
    elif a < 0 and b > 0:
        print("Koordinata naxodistya v 2 chetverti")
    elif a > 0 and b < 0:
        print("Koordinata naxoditsya v 4 chetverti")
    elif a < 0 and b < 0:
        print("Koordinata naxoditsya v 3 chetverti")
    else:
        print("Wrong value")

koordina(23,-23)
koordina(-23,23)
koordina(23,23)
koordina(-23,-23)




#Определите сколько в числе чётных цифр, и сколько нечётных. Число вводиться с клавиатуры
def kalkulyator(a):
    list_empty = (str(a))
    juft = 0
    toq = 0
    for i in list_empty:
        intList = int(i)
        if intList % 2 == 0:
            juft += 1
        else:
            toq += 1
    print("Adadi juft: " + str(juft) + " adad", "\nAdadi toq: " + str(toq) + " adad")
kalkulyator(123456789)


