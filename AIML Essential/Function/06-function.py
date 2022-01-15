# write a function which returns and joins strings ina a list

a = ["Welcome","to","edureka"]

def add_elementsOfList(data):
    finalOutput = "";
    for ele in range(len(data)):
        finalOutput = finalOutput + data[ele] + " "
    return finalOutput

b = add_elementsOfList(a)

print(b)