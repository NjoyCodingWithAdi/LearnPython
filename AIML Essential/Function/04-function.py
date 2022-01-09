# pass a list of fruits of fruits and it should printr allfruit names with default concept

def fruit(fruitNames = ['Apple', 'Orange', 'Mango']):
    print(fruitNames)
    
fruit()

# second way without default

input = ['Apple', 'Orange', 'Mango']

def fruits(input):
    for i in input:
        print(i)
    
fruits(input)