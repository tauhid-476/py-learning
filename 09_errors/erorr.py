
file = open('youtube.txt','w')

try:
    file.write("chai aur py")
finally:
    file.close()

# same as above
with open('youtube.txt', 'w') as file:
    file.write("chai aur py")