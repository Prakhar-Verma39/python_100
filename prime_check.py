def prime_checker(number):
    isPrime = True
    if(number > 1 ):
        integer = 2
        while integer ** 2 <= number:
            if(number % integer == 0):
                isPrime = False
                break
            if integer == 2:
                integer += 1
            else:
                integer += 2
        if(isPrime):
            print("Is a prime")
        else:
            print("Not a prime")

n = int(input("Check this number: "))
prime_checker(number=n)