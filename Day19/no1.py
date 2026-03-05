f = open('PesanSederhana.txt','r')

lines = f.readlines()
print(type(lines))
print(lines)
f.close()

import json

person_json ='''{"name":"Handy","country":"Indonesia","city":"Surabaya","skills":["Javascript","C++","C","Python"] }'''

person_dct = json.loads(person_json)

print(type(person_dct))
print(type(person_json))
print(person_dct)
print(person_dct['skills'])
