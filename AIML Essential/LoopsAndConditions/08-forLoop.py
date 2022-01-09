# write a code whose output should be

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = 5

for i in range(1, n+2):
    for j in range(1, i):
        print(j, end = " ")
    print("\n")
    

word = ""
for i in range(1,6):
    word = word + str(i) + ""
    print(word)