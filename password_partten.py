import re
def is_valid_password(password):
    password =input("Enter your password: ")

    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$#]).+$'
    return bool(re.match(pattern, password))
print(is_valid_password(""))