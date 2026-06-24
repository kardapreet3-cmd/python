import re
def is_valid_mobile(number):
    number =input("Enter your mobile number: ")
    pattern = r'^[0-9]{10}$'
    return len(number)==10 and number.isdigit()
print(is_valid_mobile("123"))