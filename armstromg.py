def is_amg(num):
    digits = len(str(num))
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    if total == num:
        print(num, "is an Armstrong Number")
    else:
        print(num, "is not an Armstrong Number")

is_amg(153)
is_amg(123)