def check_season(month):
    Autumn = ['september','october','november']
    Winter = ['december','january','february']
    Spring = ['march','april','may']
    Summer = ['june','july','august']
    print(f"You enter {month}.")
    if month.lower() in Autumn:
        print(f"The season of {month} is Autumn.")
    elif month.lower() in Winter:
        print(f"The season of {month} is Winter.")
    elif month.lower() in Spring:
        print(f"The season of {month} is Spring.")
    elif month.lower() in Summer:
        print(f"The season of {month} is Summer.")
    else:
        print("Please input a correct month!")


check_season('april')