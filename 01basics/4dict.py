
chai_dict = { "masala":"spicy","ginger":"zesty","green":"mild"}

print(chai_dict["masala"])

print(chai_dict.get("masalaa")) #no error
# print(chai_dict["masalaa"]) #gives error


chai_dict["green"] = "sweet"
print(chai_dict.get("green")) #no error

for c in chai_dict:
    print(c, chai_dict[c])

for key, value in chai_dict.items():
    print(key, value)


if "masala" in chai_dict:
    print("I have masala chai") 

# insert a value
chai_dict["Earl Grey"] = "Citrus"
print(chai_dict)

chai_dict.pop("ginger")
print(chai_dict)

# remvse last elm
chai_dict.popitem()
print(chai_dict)

del chai_dict["green"]
print(chai_dict)

tea_shop = {
    "chai": {"Masala":"Spicy","Ginger":"Zesty"},
    "Tea": {"Green":"Mild","Black":"Strong"}
}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["Tea"])

print(tea_shop["chai"]["Masala"])

squared_nums = { x: x**2 for x in range(10)}
print(squared_nums)

cube_nums = { y:y**3 for y in range(10)}
print(cube_nums)

squared_nums.clear()

keys = ["Masala","Ginger","Lemon"]
default_vals = "Delicious"


new_dict = {key: default_vals for key in keys}
print(new_dict)

new_dict2 = dict.fromkeys(keys, default_vals)
print(new_dict2)