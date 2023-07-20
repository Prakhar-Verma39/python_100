scores = input("Enter the scores of the test").split(' ')
max = 0 
for score in scores:
    if int(score) > max:
        max = int(score)
print(f"Highest score: {max}")