phrase = 'Coding For All'
phrase2 = 'Coding For All People'

print(phrase.find('C'))
print(phrase.find('F'))
print(phrase2.rfind('I'))

phrase3 = 'You cannot end a sentence with because because because is conjunction'

print(phrase3.find('because'))
print(phrase3.rfind('because'))

slice_because = phrase3[31:54]
print(slice_because)

print(phrase.endswith('Coding'))
print(phrase.startswith('Coding'))

phrase4 = '   Coding For All      ' 

print(phrase4.strip(' '))

libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result ='# '.join(libraries)
print(result)

sentences = 'I am enjoying this challenge.\nI just wonder what is next.'
print(sentences)

print('Name\tAge\tCountry\t\tCity')
print('Handy\t33\tIndonesia\tSurabaya')

radius = 100
pi = 3.14
area = pi*radius**2

formated_strings = 'Radius = {}.\nArea = {}*{}**2.\nThe area of a circle with a radius {} is {:.3f}.'.format(radius,pi,radius,radius,area)
print(formated_strings)

a = 8
b = 6

print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.3f}'.format(a,b,a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))
