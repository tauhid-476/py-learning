age = int(input("Please enter your age:\n"))
day = str(input("Please enter the booking day\n"))

price = 12 if age > 18  else 8
price -=2 if day =="Wednesday" else price
print(price)