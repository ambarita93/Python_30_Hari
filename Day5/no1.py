empty_list = []
list1 = [1,2,3,4,5,6,7,8,9]
length_of_list = len(list1)
print(length_of_list)
print(list1[0],list1[4],list1[-1])

mixed_data_types = ['handy',33,163,'married','surabya']
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(mixed_data_types)
print(it_companies)
print(len(it_companies))

print(it_companies[0],it_companies[3],it_companies[-1])
it_companies.insert(0,'Starlink')
it_companies[2] = it_companies[2].upper()

print(it_companies)
join_it_companies='# '.join(it_companies)
print(join_it_companies)

it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

print(it_companies[0:3]) #first 3 item
print(it_companies[-3:]) #last 3 item
print(it_companies[3:5]) #middle item
first_it_companies = it_companies[0]
middle_it_companies = it_companies[3]
last_it_companies = it_companies[-1]
it_companies.remove(first_it_companies)
print(it_companies)
it_companies.remove(middle_it_companies)
print(it_companies)
it_companies.remove(last_it_companies)

print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML','CSS','JS','React','Redux']
back_end = ['Node','Express','MongoDB']

full_stack = front_end + back_end

full_stack.insert(5,'Python')
full_stack.insert(5,'SQL')
print(full_stack)