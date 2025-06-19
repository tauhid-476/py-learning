
age = int(input("Please enter your age:\n"))

if age < 13 and age > 0:
    print("Child")
elif age > 13 and age < 19:
    print("Teenager")
elif age < 60 and age > 19:
    print("Adult")
elif age > 60:
    print("Sen Citzn")    
else:
    print("Invalid age")            