import random

no_of_letters = int(input("Welcome to the PyPassword Generator!\nHow many letters would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))
no_of_numbers = int(input("How many numbers would you like?\n"))

# ord() function in Python. Python ord() function returns the Unicode code from a given character. This function accepts a string of unit length as an argument and returns the Unicode equivalence of the passed argument.


letters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
letters += [chr(x) for x in range(ord('A'), ord('Z') + 1)]
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-','.',',','[',']','{','}',';',':','/','?','<','>','"',"'",'|','~','`']
numbers = [x for x in range(0,10)]
password = ""

for n in range(0,no_of_letters):
    password += letters[random.randint(0,len(letters) - 1)]
for n in range(0,no_of_symbols):
    password += symbols[random.randint(0,len(symbols) - 1)]
for n in range(0,no_of_numbers):
    password += str(numbers[random.randint(0,len(numbers) - 1)])

# Need a list to perform shuffling via random module shuffle method
password = list(password)

# Perform shuffling via random module shuffle method
random.shuffle(password)

# Convert list to string
password = ''.join(password)

# Print password as a String
print("Here is your password: ",password)