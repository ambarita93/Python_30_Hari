person={
    'first_name': 'Handy',
    'last_name': 'Ambarita',
    'age': 33,
    'country': 'Indonesia',
    'is_married': True,
    'skills': ['Node','Javascript', 'Python', 'C++', 'CSS', 'HTML','Java','React','MongoDB'],
    'address': {
        'street': 'Space street',
        'zipcode': '60111'
    }
    }

if person['skills'] is None:
    print('The skills is none.')
else:
    print(person['skills'])

if 'Python' in person['skills']:
    print("One of his skills is Python.")
else:
    print("He doesn't have Python skills.")

skills_of_front_end = {'Javascript','React'}
skills_of_back_end = {'Node','Python','MongoDB'}
skills_of_full_stack ={'React','Node','MongoDB'}

my_skills = set(person['skills'])

if skills_of_front_end.issubset(my_skills) and my_skills.issubset(skills_of_front_end):
    print("With his skills:{}, he can be a front end developer.".format(skills_of_front_end))
elif skills_of_back_end.issubset(my_skills):
    print("With his skills:{}, he can be a back end developer.".format(skills_of_back_end))
elif skills_of_full_stack.issubset(my_skills) and my_skills.issubset(skills_of_full_stack):
    print("With his skills:{}, he can be a fullstack developer.".format(skills_of_full_stack))
else:
    print("Given his skills ({}), he needs one more languange to determine his career path.".format(my_skills))

if person['is_married'] is True and person['country'] is 'Indonesia':
    print('{} {} lives in {}. He is Married'.format(person['first_name'],person['last_name'],person['country']))
else:
    print("Information is not enough.")