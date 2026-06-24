#partten   = r'^[\w\.-]+@[\w\.-]\.\w+$'
import re
def is_valid_email(email):
    email=input("Enter your email address: ")
    parttern = r'^[\w\'-]+@[\w\.-]+\.\w+$'
    return bool(re.match(parttern, email))
print(is_valid_email(email=""))