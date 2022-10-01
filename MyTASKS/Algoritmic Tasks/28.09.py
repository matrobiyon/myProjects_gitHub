# a =int(input("Vvedite chislo: "))
# summa = 0
# mul=1


# while a>0:
# 	b = a%10
# 	summa =summa + b
# 	mul = mul * b
# 	a = a//10


# print(summa)
# print(mul)

#40
#1 usul
a = 3242
int_to_str = str(a)
print(int_to_str[::-1])
#2usul
a = 324234
list1 = []
while a >0:
	b= a %10
	list1.append(b)
	a //=10
a = str()

for i in list1:
	int_to_str = str(i)
	a +=int_to_str

print(a)

