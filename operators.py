#arithmetic operator
a=10
b=20
print("addition: ",a+b)
print("substraction: ",a-b)
print("multiplication: ",a*b)
print("division: ",a/b)
print("floor division: ",a//b)
print("modulas: ",a%b)
print("race too power: ",a**b)

#input from user with float value arithmetic operator
c=float(input("enter a number: "))
d=float(input("enter another number: "))
print("addition: ",c+d)
print("substraction: ",c-d)
print("multiplication: ",c*d)
print("division: ",c/d)
print("floor division: ",c//d)
print("modulas: ",c%d)
print("race too power: ",c**d)


#reletional operators
e=5
f=6
print("equal too: ",a==b)
print("not equal too: ",a!=b)
print("greater than: ",a>b)
print("less than: ",a<b)
g=9
h=10
print("greater than or equal too: ",g>=h)
i=1
j=-10
print("less than or equal too: ",i<=j)

#vote
age=int(input("enter your age: "))
if age>=18:
    print("your age is",age)
    print("you are eligible for vote")
else:
    print("your age is",age)
    print("you are  not eligible for vote")


#Logical operators
#AND
print(True and False)
print(True and True)
print(False and False)
print(False and True)

#OR
print(True or False)
print(True or True)
print(False or False)
print(False or True)

#NOT
print(not True)
print(not False)


#percentage if-else
marks=float(input("enter your marks: "))
if marks>=40:
    print("PASS")
if marks>=75:
    print(" CONGRATULATION YOU GOT IT,PASS")
else:
    print("better luck next time")

#prg using relational n logical operator combine
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
print("num1>num2 and num1>0: ",num1>num2 and num1>0)
print("num1<num2 or num2>0: ",num1<num2 or num2>0)
print("not(num1==num2): ",not(num1==num2))


#eligible for driving or not

age1=int(input("enter your age: "))
license=(input("Do you have license"))
if(age1>=18 and license=="yes"):
    print("You are eligible for driving")
else:
    print("You are not eligible for driving")

#even or odd
nume=int(input("enter your number: "))
print("your number is",nume)
if(nume%2==0):
    print("your number is even")
else:
    print("your number is odd")
