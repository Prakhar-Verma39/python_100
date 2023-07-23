

print("Welcome to the secret auction program.")

bid={}

def add_new_bid(name, amount):
    bid[name]=amount


while True:
    name = input("What is your name?: ")
    amount = int(input("What's your bid? $"))

    add_new_bid(name,amount)

    ask = input("print 'yes' or 'no'")
    if ask == "yes":
        continue
    if ask == "no":
        max = 0
        for name in bid:
            if bid[name] > max:
                max = bid[name]
                ask = name
        print("Max bid: ", ask)
        break