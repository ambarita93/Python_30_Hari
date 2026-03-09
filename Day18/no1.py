import re

text =  'I love to learn Python and Javascript'

match = re.match('I love to learn',text,re.I)

print(match)

span = match.span()
print(span)
start,end = span
print(start,end)
substring = text[start:end]
print(substring)


#Data Science From Scratch.pdf

from matplotlib import pyplot as plt

years = [year for year in range(1950,2020,10)]
gdp = [300.2,543.3,1075.9,2862.5]


