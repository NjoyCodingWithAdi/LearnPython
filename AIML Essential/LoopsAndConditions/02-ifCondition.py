# User should enter two numbers x, y and then print whether x>y, x<y or x=y

x = int(input("Please enter first number :- "))
y = int(input("Please enter the second number number :- "))

if (x>y) :
    print(x, "is greater than " , y)
elif (x<y):
    print(x, "is less than " , y)
else :
    print(x, "is equal to " , y)
