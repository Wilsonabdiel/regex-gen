import re

def generate_regex(test_cases):
    regex = ''
    for test_case in test_cases:
        for char in test_case:
            if char.isalpha():
                regex += '[a-zA-Z]' if char.lower() == char else '[A-Z]'
            elif char.isdigit():
                regex += '[0-9]'
    return regex

# Usage:
test_cases = input ("Enter your input: ")
regex = generate_regex(test_cases)
print(f'Regular expression: {regex}')
