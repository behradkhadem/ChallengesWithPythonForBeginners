from math import *
from numpy import arange   #we can't use float numbers in range functor. thus, we use NumPy!

start = float(input("Please enter the beginning point. : "))
end = float(input("Please enter the ending poin. : "))
delta = float(input("Please enter the error. : "))

def func (x):
    """
    the function below can change.
    This one is:
    exp(x**2) + ([|x|])! + Sinh((pi)/x)
    """
    #y = sin(x) #this one was for test!
    y = exp(x**2) + factorial(floor(abs(x))) + sinh((pi)/x)
    return y

def integral (start, end, delta):
    '''
    as you know, we can't use float numbers in range functor. thus we use NumPy!
    arange is somthnig in Numpy
    this function will return the value as an integer number.
    '''
    value = 0
    for diff in arange(start, end+delta, delta):
        value = value + (delta * (func (diff)))
    return value

print(integral(start, end, delta))
