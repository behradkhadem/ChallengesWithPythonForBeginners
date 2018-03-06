#Stage one
for x in range(36):
    for y in range(36):
        if x + y == 35:
            if 2*x + 4*y ==94:
                print ("Yooho! we have {} chickens and {} rabbits!" .format(x, y))
                break

#####################################################################
#stage two:
'''
def animalCounter(legs, heads):
    #this function takes the legs and heads as an input and calculates the rest. 
    for x in range(heads):
        for y in range(heads):
            if x + y == heads:
                if 2*x + 4*y ==legs:
                    return ("Yooho! we have {} chickens and {} rabbits!" .format(x, y))
                    #break
                else:
                    return("unsolveble! ")
legs = int(input("enter the legs. "))
heads = int(input("enter the heads. "))
print(animalCounter(legs, heads))
'''

#####################################################################
#stage three:
'''
def animalCounter(legs, heads):
    #this function takes the legs and heads as an input and calculates the rest. 
    for x in range(heads):
        for y in range(heads):
            if x + y == heads:
                if 2*x + 4*y ==legs:
                    return (True)
                    #break
                else:
                    return(False)

def possibleAnimalCount(num):
    #it takes a number as the range and calculates the possibile "leags and heads" numbers and adds them into a dictionary and returnes it.
    possibilities = {}
    for legs in range(num):
        for heads in range(num):
            if animalCounter(legs, heads) == True:
                possibilities [heads] = legs #adds the possible legs and heads numbers into a dictionary.
    return(possibilities)

print(possibleAnimalCount(500))
'''