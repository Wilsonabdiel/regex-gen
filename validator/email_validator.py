import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return True
    else:
        return False



# Use case
    
# from email_validator import validate_email

# Get the user's email from your application
# user_email = get_user_email()  # Replace this with your actual function

# Validate the email
# if validate_email(user_email):
    # print(f'{user_email} is a valid email address.')
# else:
    # print(f'{user_email} is not a valid email address.')
