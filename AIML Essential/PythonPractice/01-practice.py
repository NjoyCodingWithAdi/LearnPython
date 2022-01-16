# Function 1
# to generate a random password --> password may contain special character
# Use random(package), inbuilt library
# random inside numpy

# Solution 1

import string
import random
 
def generate_password(length):
    all_char = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for char in range(length):
        rand = random.choice(all_char)
        password = password + rand
    return password
 
length = int(input('How many characters in your password? :-'))
print('Your new password: ',generate_password(5))


# Function 2
# Pass person's name : Test One
# test.one@gmail.com

def email_gen(name):
    name = name.split()
    email = '.'.join(name)
    return email.lower()+'@gmail.com'

print(email_gen('Test One'))

