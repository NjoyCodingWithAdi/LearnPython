def isPrime(n):
      
    # Corner case
    if n <= 1:
        return False
  
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;
  
    return True
  
# Driver Program to test above function
print("The number is prime number") if isPrime(int(input("Enter a number :-"))) else print("The nuber is not prime number")

  