import re


text = " Stripping String "

def strip_text(text, remove=''):
    if remove == '':
        space_regex = re.compile(r'(^\s*)(.*)(\s*$)')
        trimmed_string = space_regex.search(text)
        return trimmed_string.group(2)

    else:
        clean_string = re.sub(remove, "", text)
        return clean_string

user_text = input('Enter your text here: ')
user_remove = input('Enter the character you want stripped here'
                    ' (Removes Space as Default): ')

print(strip_text(user_text, user_remove))



