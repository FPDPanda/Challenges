print("This program tests a number to check if it is PRIME\n\n")
c = 0

while True:
    number = input("Please input the number you would like to test: ")
    try:
        number = int(number)
    except ValueError:
        print("Please input a valid number.")
        continue
    if number < 0:
        print("Please input a positive number")
        continue
    for n in range(1, number + 1):
        if number % n == 0:
            c += 1
    is_prime = c == 2
    if is_prime == True or number <= 3:
        print("Your number is prime.")
    else:
        print("Your number is not prime.")
    c = 0