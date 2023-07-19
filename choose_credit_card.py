import random

names = input("enter the names : \n").split(", ")

pick = random.randint(0, len(names) - 1)
print(names[pick])