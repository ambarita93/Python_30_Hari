class Person:
    def __init__(self,first_name,last_name,age,city,country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country

    def person_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old. He lives in {self.city}, {self.country}.'

p = Person('Handy','Ambarita',33, 'Surabaya')
print(p.first_name)
print(p.city)
print(p)