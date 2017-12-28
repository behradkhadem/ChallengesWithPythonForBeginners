num = int(input("Please enter an integer number. : "))
power = float(input("Please enter grade of the root : "))
err = float(input("Please enter a float number as the error. : ")) #It can't be too small.

def superRoot (num, power, err):
    '''
    This Function is not efficient but it's very simple! 
    for advanced programs, they use the Newton-Raphson function to 
    calculate the roots of a number. in this function, the error is zero. 
    but in ours, it isn't! We define the error!
    '''
    value = 0
    while (value + err)**power < num: # when the (value + err)**power >= happens, the loop stops. 
        value = value + err
    return value

print(superRoot(num, power, err))
