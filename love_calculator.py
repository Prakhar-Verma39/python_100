print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

h = l = 0
for letter in "true":
    h += (name1 + name2).count(letter)
for letter in "love":
    l += (name1 + name2).count(letter)
love_score = int(h)*10 + int(l)

print(f"Your love is {love_score}%")