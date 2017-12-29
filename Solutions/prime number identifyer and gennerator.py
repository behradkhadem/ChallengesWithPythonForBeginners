def isPrime (num):
    """
    if the prime factors are more than 2, then it is not prime! that simple!
    """
    factors = 0
    for dnum in range(1, num+1, 1): #dnum: denuminator
        if (num % dnum) == 0:
            factors = factors + 1
            if factors > 2:
                break
        else:
            pass
    if factors == 2 :
        return True
    else:
        return False


#print(isPrime(1))

def primeGenerator (num):
    """
    now we are going to generate the prime numbers!
    we are going to add them into a list!
    """
    primes = []
    for each in range(1, num):
        if isPrime(each) is True:
            primes.append(each)
        else:
            pass
    return primes

print(primeGenerator(10000))


#I've found this piece of code in Stack overflow. I quite don't understand the algorithm of this code. but it's very efficient. 

'''
def makePrime(n):
    numbers = set(range(n, 1, -1)) #We add the numbers between 1 and n (step=1) in a set. 
    primes = [] #an empty list.
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p))) #what happens here?
    return primes

print(makePrime(10000000))

'''