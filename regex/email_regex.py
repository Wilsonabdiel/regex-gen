import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return True
    else:
        return False

# Usage:
email = input('Enter your email: ')
if validate_email(email):
    print(f'{email} is a valid email address.')
else:
    print(f'{email} is not a valid email address.')
