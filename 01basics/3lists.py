tea_varieties = ["Masala", "Mint", "Oolong", "Black"]

print(tea_varieties[-1])

last_elm = tea_varieties[len(tea_varieties) - 1]
print(last_elm)

print(tea_varieties[1:2])

# tea_varieties[1:2] = "Lemon"
# cause problem , insert each letter as an array element
tea_varieties[1:2] = ["Lemon"]
print(tea_varieties)
# ['Masala', 'Lemon', 'Oolong', 'Black']

tea_varieties[1:3] = ["white", "brown"]
print(tea_varieties)
# ['Masala', 'white', 'brown', 'Black']

tea_varieties[1:1] = ["test","test"]
print(tea_varieties)
# ['Masala', 'test', 'test', 'white', 'brown', 'Black']

tea_varieties[1:3] = []
print(tea_varieties)
# ['Masala', 'white', 'brown', 'Black']

for tea in tea_varieties:
    print(tea)

for tea in tea_varieties:
    print(tea,end="-")
    # Masala-white-brown-Black-


tea_varieties.append("Oolong")
print(tea_varieties)

if "Oolong" in tea_varieties:
    print("Yes i have it")
else:
    print("I do not have it")

tea_varieties.pop()
print(tea_varieties)

tea_varieties.remove("Masala")
print(tea_varieties)

tea_varieties.insert(0, "Masala")
print(tea_varieties)

tea_varieties_copy = tea_varieties.copy()
# prevents both pointing to same in the memory

tea_varieties_copy.append("Lemon")
print("Tea varieties:",tea_varieties)
print("Tea varieties copy:",tea_varieties_copy)

squared_nums = [x**2 for x in range(10)]
print(squared_nums)
# all squares from 0 to 9

cube_nums = [y**3 for y in range(5)]
print(cube_nums)