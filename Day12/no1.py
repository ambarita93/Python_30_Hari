import secrets
import string

def random_user_id():
    random_string = ''.join(secrets.choice(string.ascii_letters+string.digits) for i in range(8))
    return random_string

print(random_user_id())

def user_id_gen_by_user():
    input1 = int(input("Number of char: "))
    input2 = int(input("Number of ID to be generated: "))

    for i in range(input2):
        random_string = ''.join(secrets.choice(string.ascii_letters+string.digits) for i in range(input1))
        print(random_string)

user_id_gen_by_user()