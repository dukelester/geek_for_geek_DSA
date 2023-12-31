''' A String is a data structure in Python that represents a sequence of characters.
It is an immutable data type, meaning that once you have created a string, you cannot change it.
Strings are used widely in many different applications, such as storing and manipulating text data,
representing names, addresses, and other types of data that can be represented as text.
'''
import re

print('Welcome to pythin strings ')

test = 'test'
test2 = "test 2"

print(test, test2)

# access elements
full_name = 'Duke Lester'
print(full_name[0], full_name[-1])
string = 'GeeksForGeeks'
print(string[3:10], string[3:-3])

reversed_string = string[::-1]
print(reversed_string)

print(''.join(reversed(full_name)))

list_string = list(full_name)
list_string[7] = 'H'
print(list_string)

print(re.match('hello', 'duke lester hello'))

def check_vowels(string3, vowels):
    result = [ d for d in string3 if d in vowels ]
    print(result) 
    return len(result)
vowels = 'aeiou'
print(check_vowels('duke lester is amazing', vowels))


# Check the validity of the password
def check_pass_validity(password_string):
    valid = ''
    while True:
        if len(password_string) < 8:
            valid = False
            break
        if not re.search('[a-z]', password_string):
            valid = False
            break
        if not re.search('[A-Z]', password_string):
            valid = False
            break
        if not re.search('[0-9]', password_string):
            valid = False
            break
        if not re.search('[_*&$#@!]', password_string):
            valid = False
            break
        if re.search('\rs', password_string):
            valid = False
            break
        valid = True
        print('The password is valid')
        break
    if not valid:
        print('The password is invalid!!')
print(check_pass_validity('dukelester'), check_pass_validity('R@m@_f0rtu9e$'))


def find_urls(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [ x[0] for x in url ]

print(find_urls('''My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles
                in the portal of https://www.geeksforgeeks.org/'''))

def find_other_urls(string2):
    ''' Use the startswith method
    '''
    my_string = string2.split()
    result = []
    for i in my_string:
        if i.startswith('https') or i.startswith('http'):
            result.append(i)
    return result
text = '''My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles
in the portal of https://www.geeksforgeeks.org/
'''
print(find_other_urls(text))

def find_urls_using_find(text):
    '''Use the find method to find the urls '''
    my_text = text.split()
    result = []
    for i in my_text:
        if i.find('https') == 0 or i.find('http') == 0:
            result.append(i)
    return result

print(find_urls_using_find(text))
