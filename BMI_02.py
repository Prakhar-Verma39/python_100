height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in Kg: "))
BMI=int(weight//height**2)
show = ""
if BMI < 18.5:
    show="underweight"
elif 18.5 < BMI < 25:
    show="normal weight"
elif 25 < BMI < 30:
    show="overweight"
elif 30 < BMI < 35:
    show="obese"
elif 35 < BMI:
    show="clinically obese"
print(f"Your BMI is {BMI}, you are " + show)