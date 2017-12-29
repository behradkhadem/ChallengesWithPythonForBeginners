from math import *

x = float(input("Please enter a random number. : "))
delta = float(input("please enter the value of error. (Don't make it too small! 0.000001 is a good value for instance.) : "))

def func (x):
    """the function below can change.
    This one is:
    exp(x**2) + ([|x|])! + Sinh((pi)/x)
    """
    y = exp(x**2) + factorial(floor(abs(x))) + sinh((pi)/x)
    return y

def derive (x, delta):
    "now we calculate the derived value with an error of delta!"
    num = func(x) - func(x-delta)
    denum = delta
    m = num / denum
    return m

print(derive(x, delta))
