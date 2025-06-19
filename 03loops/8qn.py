
n = int(input("Enter a number:\n"))

is_prime = True

if n > 1:
    for i in range(2,n):
        if (n % i) == 0:
            is_prime = False
        else:
            continue

print(is_prime)
