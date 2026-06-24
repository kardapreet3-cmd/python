# syntax :
# lambda srgument: expression
#eg::    square = lambda x:x*X
# fun without a name is a lambda
from asyncio import create_subprocess_exec

addition=lambda a,b:a+b
print(addition(3,4))



square =lambda x:x*x
print(square(3))

#map()
numbers=[1,2,3,4,5,6,7,8,9,10]
squares=list(map(lambda x: x*x,numbers))
print(squares)

#filter()
number=[10,20,30,40,50,60,70,80,90,100]
even = list(filter(lambda x:x%2==0,numbers))
print(even)

#cube
cube=lambda x:x**3
for i in range(5):
    num=int(input(f" Enter a number {i+1}: "))
    print("Cube is: ",cube(num))