class Person:
    def __init__(self,first_name,last_name,age,city,country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
        self.skills = [] 

    def person_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old. He lives in {self.city}, {self.country}.'
    def add_skils(self,skill):
        self.skills.append(skill)

class Student(Person):
    def __init__(self, first_name, last_name, age, city, country,gender):
        self.gender = gender
        super().__init__(first_name, last_name, age, city, country)
    def person_info(self): # fungsi dari kelas Person (super) yang di-override 
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.first_name} {self.last_name} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'



p = Person('Handy','Ambarita',33, 'Surabaya','Indonesia')
print(p.first_name)
print(p.city)

p2 = Person('Mateo','Ambarita',3,'Surabaya','Indonesia')
p2.add_skils('Singing')
print(p2.skills)

p3 = Student('Samuel','Ambarita',23,'Jambi','Indonesia','male')
print(p3.person_info())