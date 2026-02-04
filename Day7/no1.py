it_companies = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
A = {19,22,24,20,25,26}
B = {19,22,20,25,26,24,28,27}
age = [22,19,24,25,26,24,25,24]

length_of_it_companies = len(it_companies)

print(length_of_it_companies)
it_companies.add('Twitter')
it_companies.update(['Zero One','Indosat','Biznet','GitHub'])
print(it_companies)

it_companies.remove('Indosat')
print(it_companies)
it_companies.discard('Biznet')# if one uses the 'discard' method, no errors will be raised if the item is not in the set.


C = A.union(B)

print(A.intersection(B))

print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))

del A,B
age_lst = set(age)
print(age_lst)

print(len(age)>len(age_lst))

phrase = 'I am a teacher and I love to inspire and teach people.'
split_phrase = phrase.split()
print(split_phrase)
split_phrase_st = set(split_phrase)
number_of_unique_words = len(split_phrase_st)
print("There are {} unique words in '{}'.".format(number_of_unique_words,phrase))