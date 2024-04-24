class Animal:
    def __init__(self, legs):
        print("animal Created")
        self.legs = legs
    def whoAmI(self):
        print("i am an animal")
    
class Bird(Animal):
    def __init__(self, legs, wings):
        super().__init__(legs)
        self.wings = wings
    def fly(self):
        print("birds can fly")

a = Animal(4)
b = Bird(2)

