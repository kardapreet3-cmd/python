import re

def validate_email(email):
    email = input("Enter your email address: ")
    parttern = r'^[\w\'-]+@[\w\.-]+\.\w+$'
    return bool(re.match(parttern, email))
print(validate_email(email=""))
def validate_password(password):
    password = input("Enter your password: ")
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$#]).+$'
    return bool(re.match(pattern, password))
print(validate_password(""))
import hashlib
def generate_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()
password = input("Enter Password: ")

hashed_password = generate_hash(password)

print("Hashed Password:", hashed_password)

def register_user(email,password):
    if validate_password(password) and validate_email(email):
        print("successfully registered")
    else:
        print("Sorry, something  is incorrect")
register_user(email="",password="")

