
# First non-repetetive char

input_str = "teeters"

for c in input_str:
    char_count = input_str.count(c)
    if char_count == 1:
        print(c)
        break