class Animal:
    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        print("Meow")
class Dog(Animal):
    def sound(self):
        print("Woof")
def make_sound(animal):
    animal.sound()
cat = Cat()
dog = Dog()
make_sound(cat)  
make_sound(dog)  
