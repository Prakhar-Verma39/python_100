import art2

print(art2.logo)
first = int(input("What's the first number?: "))

def perform_op(first,op,second):
    if op == "+":
        return first + second
    elif op == "-":
        return first - second
    elif op == "*":
        return first * second
    elif op == "/":
        return first / second

while True:
    op = input("+ \n - \n * \n / \n Pick an operation: ")
    second = int(input("What's the next number?: "))
    
    ans = perform_op(first,op,second)
    print(str(first) + " " + op + " " + str(second) + " " + "="+" "+ str(ans))
    i = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ")
    if i == "y":
        first = ans
    elif i == "n":
        print(art2.logo)
        first = int(input("What's the first number?: "))
