countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def upper_name(country):
    return country.upper()

def square(number):
    return number ** 2

def land_country(country):
    if country.endswith('land'):
        return True
    return False

def six_char_country(country):
    if len(country)==6:
        return True
    return False

def E_detected(country):
    if country[0] == 'E':
        return True
    return False

#map
uppercase_countries = list(map(upper_name,countries))
square_number = list(map(square,numbers))
uppercase_name = list(map(upper_name,names))

#filter
country_land = list(filter(land_country,countries))
country_with_six_char = list(filter(six_char_country,countries))
e_country = list(filter(E_detected,countries))

print(uppercase_countries)
print(square_number)
print(uppercase_name)
print(country_land)
print(country_with_six_char)
print(e_country)
