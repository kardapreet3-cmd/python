#prime numbers
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
numbers = [2, 7, 10, 13, 15]
for n in numbers:
    if is_prime(n):
        print(n, "is Prime")
    else:
        print(n, "is Not Prime")

