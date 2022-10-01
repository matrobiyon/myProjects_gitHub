#41
# a = "Qosim"
# b = list(a)
# b.reverse()
# b = "".join(b)
# print(b)

# #42
# pokazatelStepeni = 2
# max_stepen = 100

# coun = 1
# res = 0

# print(pokazatelStepeni) 
# print(max_stepen)

# while res < max_stepen:
# 	res = coun ** (pokazatelStepeni)
# 	print(res, end=" ")
# 	coun += 1
# print()
# print(coun-1)

# #43
# inpit_int = 5
# coun = 1
# res = 1
# while coun < inpit_int:
# 	res *= (coun+1)
# 	coun += 1
# print(res)

# import math
# a = math.factorial(5)
# print(a)

#44
# n = 10
# fib1, fib2 = 1,1
# print(fib1,fib2,end=" ")
# while n > 2:
# 	fib3 = fib1 + fib2
# 	print(fib3, end=" ")
# 	fib1 = fib2
# 	fib2 = fib3
# 	n -= 1

#45
# i = 1
# for i in range(32,127):
# 	print(chr(i), end=" ")
# 	if (i-1) % 10 ==0:
# 		print()

# #46
# from random import randint
# a = randint(1,101)	
# while False:
# 	input_int = int(input(" : "))
# 	if input_int > a:
# 		print("Mnogo")
# 		continue
# 	elif input_int < a:
# 		print("Malo")
# 		continue
# 	else:
# 		print("Vi ugadali", a)
# 		break


# #51
# a = 0.8
# res = a
# n = 4
# for i in range(1,n):
# 	res *=(a+i)
# print(res)

# #52
# a = 1
# summa = 0
# pol = 5

# for i in range(pol):
# 	summa += a
# 	a /= -2

# print(summa)

#53
# a = 1
# b = 2
# c = 0.001
# count = 0
# res = 0
# sign = 1
# while a/b > 0.001:
# 	print(a/b)
# 	res += sign * a/b
# 	count +=1
# 	a += 1
# 	b *= 2
# 	sign = -sign
# print(count)
# print(res)

# #
# a = 4
# b = 2
# list1=[]
# while a >= 1:
# 	c = a%b
# 	res = a/b
# 	list1.append(int(c))
# 	a = res 

# print(list1[::-1])

# a = [{"key":"value"}, {"key": "value"}]
# def dub(a):
# 	for i in a:
# 		for j in a:
# 			if i == j:


