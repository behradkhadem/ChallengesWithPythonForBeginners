import re
email = input("Please enter your email. \n")

def checkMail(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email, re.IGNORECASE)
    if match:
        return True
    else:
        return False
