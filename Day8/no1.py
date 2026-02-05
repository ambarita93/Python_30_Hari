dog = {}
dog['name'] = 'Qwee'
dog['breed'] = 'Siberian Husky'
dog['legs'] = 'medium length'
dog['age'] = 2

student = {'first name':'Handy','last name':'Ambarita','age':33,'marital status':True,'skills':['Python','R','matlab'],'country':'Indonesia',
           'city':'Surabaya','address':{'street':'Kendangsari','zipcode':'60111'}}

print(len(student))

print(student['skills'])
print(type(student['skills']))
student['skills'].append('HTML')

del student['marital status']

print(student)

del dog