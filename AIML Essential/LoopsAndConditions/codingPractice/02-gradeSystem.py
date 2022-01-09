mark = int(input("Please enter the mark :- "))
 
if mark < 25:
    print("As your mark is less 50, your grade is F")  
elif mark >= 25 and mark <= 45:
    print("As your mark is in between 25 t0 45 your grade is E")    
elif mark >= 45 and mark <= 50:
    print("As your mark is in between 45 t0 50 your grade is D")
elif mark >= 50 and mark <= 60:
    print("As your mark is in between 50 t0 60 your grade is C")
elif mark >= 60 and mark <= 80:
    print("As your mark is in between 60 t0 80 your grade is B")
else:
    print("As your mark is above 80 and your grade is A")