class student:
    def __init__(self):
        self.name="Preet"
        self.age=17
    def edit(self,age):
        if age >=0 and age<=18:
            self.age=age
        else:
            print("can't vote")


        self.age=age
    def show(self):
        print(self.age)
s=student()
s.age=18
s.edit(18)
s.show()

