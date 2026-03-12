class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p = Person('Handy','Ambarita',33)
print(p.first_name)
print(p.age)
print(p)