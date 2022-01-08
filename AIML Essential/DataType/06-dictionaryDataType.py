#  It's presented by {}
#  Unique data type which is the combination of key value pair
#  A dictionary can contain any data types

#  Create a dictionary of names and their age
#  Dictionary is mutable

names = ['A','B','C']
ages = [3,4,5]

dic = {"name":['A','B','C'], "age":[3,4,5]}
print (dic)
print(type(dic))

#  Create a dictionary 'car' which contains the key as brands, fuel, year, colors 

car = {"brand":['Hyundai','Tata'],"fuel":[20,21],"year":[1998,1997],"colour":['blue','black']}
print(car)

print(car['brand'])

# Replace the value ['Hyundai','Tata'] to ['Maruti','Mahindra']

car['brand'] = ['Maruti','Mahindra']
print(car)