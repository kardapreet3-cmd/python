num1=int(input("enter your first number"))
num2=int(input("enter your second number "))
print(" which operation do you want to perform");
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    print("Result =", num1 + num2)
elif choice == 2:
    print("Result =", num1 - num2)
elif choice == 3:
    print("Result =", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid choice")