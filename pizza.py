print("Welcome to python Pizza Deliveries!")
size = input("What size pizza do you want?")
add_pepperoni = input("Do you want pepperoni?")
extra_cheese = input("Do you want extra cheese?")
bill = 0

if size == "L" or size == "l":
    bill += 25
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill +=3
elif size == "M" or size == "m":
    bill += 20
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 3
elif size == "S" or size == "s":
    bill += 15
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 2
else:
    print("Invalid Entry")

if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1
    print(bill)

print(f"Your final bill is: ${bill}")