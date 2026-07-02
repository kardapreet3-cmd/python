class Animal:
    def sound(self):
        print("Animal")
class Dog(Animal):
    def sound(self,name):
        self.name=name
        print(f"name is {name}")
d=Dog()
d.sound("sheru")
