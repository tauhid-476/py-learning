
password = str(input("Enter a password:\n"))

passlen = len(password)
print(passlen)

if passlen < 6:
    strength="Weak pass"
elif 6 < passlen < 10:
    strength = "MEdium"
elif passlen > 10:
    strength="Strong"

print(strength)    
              
