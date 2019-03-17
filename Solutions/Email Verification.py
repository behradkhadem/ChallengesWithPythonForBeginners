import re #Regular Expression library for Python.

def checkMail(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email, re.IGNORECASE) #we used regular expression for the hard part!
    if match:
        return True
    else:
        return False

email = input("Please enter your email. \n")
print(checkMail(email)) #It just returns True and False but you can play with it.