def palindrome(value):
    value=str(value)

    if value==value[::-1]:
        print(value, "is a palindrome")
    else:
        print(value, "is not a palindrome")
palindrome(521)
palindrome(123)
palindrome(121)
palindrome("madam")