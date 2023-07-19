print("Welcome to the tip calculator.")
t_bill=float(input("What was the total bill? $"))
n_people=int(input("How many people to split the bill? "))
percent=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
pay = t_bill*(100 + percent)/(100*n_people)
print(f"Each person should pay: ${ pay:.1f}") # F string format for printing decimal values upto certain percision.
