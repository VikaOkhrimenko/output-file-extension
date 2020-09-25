filename = input("Enter filename: ")
expansion = ''
flag = 0

for j in range(0, len(filename)):
    if filename[j] == ".":
        flag = 1
        point = j

if flag == 1:
    for j in range(point, len(filename)):
        expansion += filename[j]
else:
    print("Error... Expansion not found.")
    
print(expansion)