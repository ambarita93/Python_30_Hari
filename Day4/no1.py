word1 = 'Thirty'
word2 = 'Days'
word3 = 'Of'
word4 = 'Python'
space = ' '

sentence = word1+space+word2+space+word3+space+word4
print(sentence)

word5 = 'Coding'
word6 = 'For'
word7 = 'All'

sentence2 = word5+space+word6+space+word7
print(sentence2)

company = 'Coding For All'
print(company.upper())
print(len(company))
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

sentence3 = 'Python for Everyone'
sentence4 = sentence3.replace('Everyone','All')
print(sentence3)
print(sentence4)

sentence5 = company.split()
print(sentence5)

sentence6 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(sentence6.split(','))
print(company[0])
print(company[-1])
print(company[10])