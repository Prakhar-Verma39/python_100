row1 = ["a","a","a"]
row2 = ["a","a","a"]
row3 = ["a","a","a"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? \n"))
# position = input("Where do you want to put the treasure? \n")

map[position%10 - 1][round(position/10 - 1)] = "x"

# map[int(position[1])-1][int(position[0])-1] = "x"

print(f"{row1}\n{row2}\n{row3}")
