chai = 'Masala Chai'

first_char = chai[0]
print(first_char)

masala = chai[:6]
print(masala)

l1 = "0123456789"

print(l1[:])
# 0123456789
print(l1[0:9:2])
# 02468

chai = "   spaced chars   "
print(chai.strip())
# spaced chars

chai = "Lemon chai"
print(chai.replace("Lemon","Ginger"))

chai = "Lemon, Mint, Masala, Ginger"
print(chai.split(", "))


chai = "Masala chai"
print(chai.find("chai"))

chai = "Masala  chai chai chai chai"
print(chai.count("chai"))

chai_type = "Masala"
chai_quantity = 2
ordered = "I ordered {} cups of {} chai"
print(ordered.format(chai_quantity,chai_type))

chai_vars = ["Lemon", "Ginger", "Mint"]
print("".join(chai_vars))
# LemonGingerMint
print("-".join(chai_vars))
# Lemon-Ginger-Mint

chai = "Masala"
# for c in chai:
#     print(c)

chai = "he said , \"Masala chai is awesome\""    
print(chai)
# chai = "c:\user\pwd"
# print(chai) #Gives error
chai = r"c:\user\pwd"
print(chai)

chai = "Masala chai"
print("Masal" in chai)