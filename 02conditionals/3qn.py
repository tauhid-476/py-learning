marks = int(input("Enter your marks\n"))

if marks >= 101:
    print("Enter a valid marks\n") 
    exit()

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"  
elif marks >= 60:
    grade = "D" 
else:
    grade = "F"

print(grade)