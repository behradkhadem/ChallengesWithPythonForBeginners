#1- the most simple way! :

def facto(num):
    value, factorial = 1, 1
    for value in range(1,num):
        factorial = factorial * (value + 1)
        value = value + 1
    return(factorial)

#print(facto(5000))


#2- Using Range: 

'''
def fact1 (num):
    value = 1
    for number in range(1, num+1, 1):
        value = value * number
    return value
print(fact1(8000))
'''

#3- Recursion : we can make our problems simpler by decreasing it's level.
'''
def fact(n):
    if n == 1 :
        return 1
    else:
        return n* fact(n-1)
print(fact(120)) #the input can't be too big. test it to see it for your self.
'''

#0- for using factorial in python we can import it from math library. like this:
'''
from math import factorial
print(factorial(10000))
'''
