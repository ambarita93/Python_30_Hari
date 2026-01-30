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
