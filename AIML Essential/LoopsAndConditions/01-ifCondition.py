# Suppose we want our code to be triggered in certain condition

# Print a stetement only if a variable i.e. num > 5

# Note 1 :- Python is very sensitive to indetation
# Note 2 :- Any statement ends with colon ":"

num = int(input("Please enter a number :- "))

if num > 5:
    print(num, "is a number greater than 5")
elif num < 5:
    print(num, "is a number less than 5")
else:
    print("Number is equal to 5")