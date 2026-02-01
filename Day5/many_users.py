users = { 'hfrank':
         {'first':'handy',
          'last':'ambarita',
          'location':'Surabaya',
          },
        'mfaith':
        {'first':'mateo',
         'last':'ambarita',
         'location':'Surabaya',
        }
        }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")