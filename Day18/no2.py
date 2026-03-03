import re

txt = '''Python is the most beautiful language that human being has ever created. 
I recommend Python for a first programming language.'''

matches = re.findall('language',txt,re.I)
matches_python = re.findall('python',txt,re.I)
print(matches)
print(matches_python)