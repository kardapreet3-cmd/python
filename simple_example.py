class Animal:
    def bark(self):
        print("Dog is barking")
    def meow(self):
        print("cat is meowing")
class Dog(Animal):
    pass
class Cat(Animal):
    pass
d=Dog()
d.bark()
