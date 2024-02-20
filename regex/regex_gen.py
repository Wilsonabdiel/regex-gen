import re
import argparse

parser = argparse.ArgumentParser(description='Generate a regular expression that matches all provided test cases.')

parser.add_argument('test_cases', type=str, nargs='+', help='A list of test cases to match.')
args = parser.parse_args()

def generate_regex(test_cases):
    regex = ''
    for test_case in test_cases:
        for char in test_case:
            if char.isalpha():
                regex += '[a-zA-Z]' if char.lower() == char else '[A-Z]'
            elif char.isdigit():
                regex += '[0-9]'
    return regex

regex = generate_regex(args.test_cases)

print(f'Regular expression: {regex}')
