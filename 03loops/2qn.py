
n = int(input("Enter a numer:\n"))

sum = 0

for i in range(1,n+1):
    if i%2 == 0:
        sum+=i

print(sum)