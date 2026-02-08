input_month = input('Enter name of month: ')
month = input_month.lower()
autumn = ['september','october','november']
winter = ['december','january','february']
spring = ['march','april','may']
summer = ['june','july','august']

if month in autumn:
    print("You enter {}. It's Autumn season.".format(month))
elif month in winter:
    print("You enter {}. It's Winter season.".format(month))
elif month in spring:
    print("You enter {}. It's Spring season.".format(month))
elif month in summer:
    print("You enter {}. It's Summer season.".format(month))
else:
    print("Please, enter correct month!")