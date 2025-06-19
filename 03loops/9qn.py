items = ["apple", "banana", "orange", "apple", "mango"]

# for item in items:
#     if items.count(item) > 1:
#         print("Duplicated item is", item)
#         break
#     else:
#         continue


unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicated is:",item)
        break
    else:
        unique_items.add(item)         