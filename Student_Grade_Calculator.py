M1=int(input("Enter The Marks of Java: "))
M2=int(input("Enter The Marks of Python: "))
M3=int(input("Enter The Marks of DCN: "))
M4=int(input("Enter The Marks of UI/UX: "))
M5=int(input("Enter The Marks of MIC: "))
if (M1 < 0 or M1 > 100 or
    M2 < 0 or M2 > 100 or
    M3 < 0 or M3 > 100 or
    M4 < 0 or M4 > 100 or
    M5 < 0 or M5 > 100):
    print("Invalid Marks")
    print("Marks should be between 0 and 100")
else:
    # Subject-wise Fail Check
    if M1 < 35:
        print("Fail in Java")
    if M2 < 35:
        print("Fail in Python")
    if M3 < 35:
        print("Fail in DCN")
    if M4 < 35:
        print("Fail in UI/UX")
    if M5 < 35:
        print("Fail in MIC")

    total=M1+M2+M3+M4+M5
    per=total/5
    print("total marks: ",total)
    print("percentage is:",per)
    print("Pass")
    if per>=75:
        print("Percentage is greater than 75% which is: ",per)
        print("Distinction")
    elif per>= 60 and per< 75:
        print("Percentage is less than 75% which is: ",per)
        print("First class")
    elif per>= 50 and per< 60 :
        print("Percentage is greater than 50% and less than 60% which is: ",per)
        print("Second class")
    elif per>= 35 and per< 50:
        print("Percentage is greater than 35% and less than 50% which is: ",per)
        print("Pass")
    else:
        print("Fail")