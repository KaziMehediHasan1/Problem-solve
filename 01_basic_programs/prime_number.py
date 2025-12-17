"""num = int(input("Enter a number: "))
is_prime = True # Assume it is prime

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False # We found a divisor!
            break # No need to check further

    if is_prime:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is Not a Prime Number")
else:
    print(f"{num} is Not a Prime Number")"""
    
# prob: 2
num = 29
is_prime = True
for i in range(2,num):
    if num > i:
        if num % 2 == 0:
            is_prime = False
            break
     
if is_prime and num > 1:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
    