import re
import pyperclip


length_regex = re.compile(r'.{8,}')     # more than 8 characters
upper_regex = re.compile(r'[A-Z]+')     # at least 1 Uppercase
lower_regex = re.compile(r'[a-z]+')     # at least 1 lowercase
digit_regex = re.compile(r'[0-9]+')     # at least 1 digit


def password_checker(text):
    if length_regex.search(text) is None:
        return False
    if upper_regex.search(text) is None:
        return False
    if lower_regex.search(text) is None:
        return False
    if digit_regex.search(text) is None:
        return False
    else:
        return True


password = str(pyperclip.paste())

if password_checker(password):
    print('Your password is strong!')
else:
    print('Your password is weak, please change it!')
