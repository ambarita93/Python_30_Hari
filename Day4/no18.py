phrase = 'Python For Everyone'
print("We will make abbreviation for", phrase,'.')
print("The abbreviation is",end='\t')
for letter in phrase:
    if letter.isupper() == True:
        print(letter,end='')
    else:
        continue

print('\n')
phrase = 'Coding For All'
print("We will make abbreviation for", phrase,'.')
print("The abbreviation is",end='\t')
for letter in phrase:
    if letter.isupper() == True:
        print(letter,end='')
    else:
        continue