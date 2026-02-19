import secrets
import string

def random_user_id():
    random_string = ''.join(secrets.choice(string.ascii_letters+string.digits) for i in range(8))
    return random_string

print(random_user_id())