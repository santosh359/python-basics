n = int(input("Enter a number: "))
is_prime = True  # Assume the number is prime

if n <= 1:
    is_prime = False  # 0 and 1 are not prime
else:
    for i in range(2, n):  # Check from 2 to n-1
        if n % i == 0:
            is_prime = False  # Found a factor
            break  # No need to check more

if is_prime:
    print(n, "is a Prime number")
else:
    print(n, "is Not a Prime number")
