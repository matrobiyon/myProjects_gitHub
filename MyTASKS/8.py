from random import randint
def misol(a,b):
    x = True
    while x:
        ostatok = a % b
        if a % b  == 0:
            print("NOD: " + str(b))
            x = False
        a = b
        b = ostatok

misol(30,18)


randint_l = []
for i in range(20):
    randint_l.append(randint(1,100))
newlist = []
b = 0
while b < len(randint_l):
    if 35 < randint_l[b] < 65:
        newlist.append(randint_l[b])
        del randint_l[b]
    else:
        b += 1

print(randint_l)
print(newlist)



