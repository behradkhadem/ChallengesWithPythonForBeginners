# First, we define the upper case, lower case words and numbers. 

upperCase= "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
lowerCase= "abcdefghigklmnopqrstuvwxyz"
number = "0123456789"

#now, we define some empty lists.
upperCases=[]
lowerCases=[]
numbers=[]
others=[]

stringInput = input("Please enter a sample text: ")

for element in stringInput:
    if str(element) in upperCase:
        upperCases.append(str(element))
    elif element in lowerCase:
        lowerCases.append(str(element))
    elif element in number:
        numbers.append(str(element))
    else:
        others.append(str(element))


print("""there were {} upper case and {} lower case words in this input!
we also had {} numbers and {} other characters.
""" .format(len(upperCases), len(lowerCases), len(numbers), len(others))) #Spaces count as other characters. 


