#valueerror
name=input("Enter patient name:")
try:
    age=int(input("Enter age:"))
except ValueError:
    print("Please enter a valid age")
