empty_tuple = ()

brothers= ('Hegar','Samuel','H.Ambarita')
sisters = ('Desy','Nana','K.Simbolon')

family_members  = brothers + sisters
print(family_members)

numbers_of_siblings = len(family_members)
print(numbers_of_siblings)

first_brother, second_brother, father, first_sister, second_sister, mother = family_members

print(first_brother)

fruits = ('banana','apple','mango','strawberry')
vegetables = ('potatoes','carrot','spinach','cucumbers')
animal_product =('meat','dairy','seafood','gelatin')

food_stuff_tp = fruits + vegetables +animal_product
food_stuff_lt = list(food_stuff_tp)
middle_item = food_stuff_tp[5:7]
print(middle_item)

the_first_three = food_stuff_tp[0:3]
the_last_three = food_stuff_tp[-3:]

print(the_first_three)
print(the_last_three)

del food_stuff_tp

nordic_countries = ('Denmark','Finland','Iceland','Norway','Sweden')
print('Estonia'in nordic_countries)
print('Iceland'in nordic_countries)