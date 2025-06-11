class MyClass:
    def __init__(self):
        self.public_attribute = "I'm a public attribute"
        self._protected_attribute = "I'm a protected attribute"
        self.__private_attribute = "I'm a private attribute"
    def public_method(self):
        print("I'm a public method")
    def _protected_method(self):
        print("I'm a protected method")
    def __private_method(self):
        print("I'm a private method")
obj = MyClass()
print(obj.public_attribute)
obj.public_method()
print(obj._protected_attribute)
obj._protected_method()
print(obj._MyClass__private_attribute)
obj._MyClass__private_method()
