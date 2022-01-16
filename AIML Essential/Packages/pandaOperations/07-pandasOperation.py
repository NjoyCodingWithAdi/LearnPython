# Function 1
# to generate a random password --> password may contain special character
# Use random(package), inbuilt library
# random inside numpy

# Solution 1

import random
import numpy as np
import pandas as pd
 
sp_symbol = ['#','$','@','?', '&', '!']
def pass_gen():
  #function to generate password
  pwd = []
  caps_alpha = [chr(random.randrange(65, 65+26)) for _ in range(random.randrange(1, 4))]
  small_alpha = [chr(random.randrange(97, 97+26)) for _ in range(random.randrange(3, 6))]
  np.random.shuffle(sp_symbol)
  pwd.append(sp_symbol[0])
  num = [str(random.randrange(0,10)) for _ in range(random.randrange(1, 4)) ]
  pwd = pwd + caps_alpha + small_alpha + num
  np.random.shuffle(pwd)
  pwd = ''.join(pwd)
  return pwd


# Function 2
# Pass person's name : Test One
# test.one@gmail.com

def email_gen(name):
    name = name.split()
    email = '.'.join(name)
    return email.lower()+'@gmail.com'

print(email_gen('Test One'))


# create a dataframe which contains
# name of the employee email id and password

name1 = 'Ashwini S'
name2 = 'Vinu N'
dic = {'Name': [name1, name2],
       'Email': [email_gen(name1), email_gen(name2)],
       'Password': [pass_gen(), pass_gen()]}
df = pd.DataFrame(dic)
print(df)