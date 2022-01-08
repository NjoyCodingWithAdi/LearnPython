# In python as soon as we write a string, indexing happens automatiocally

a = "Aditya"
print(a[0])

b = a[0] + a[1]
print(b)

# Indexing in string is also possible from reverse
# Reverse indexing starts from -1
# Let's find out the index of 'I'
c = "Today is the first class of python for AIML."
print(len(c))
print(c.index('I'))

print(c[-4])