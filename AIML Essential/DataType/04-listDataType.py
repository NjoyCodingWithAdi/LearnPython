# list data type
# list is a data type which can contain any data type inside it

a = [1,2,3]
print(type(a))

b = [3,4.35,'Adi']
print(type(b))

# Double indexing - list inside list
c = [3,4.35,'Adi',[1,2,3]]
print(c[3][1])

# List are mutable
d = [1,2,3]
print(d)

d[1] = 4
print(d)