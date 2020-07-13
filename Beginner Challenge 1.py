print("This program tests a number to check if it is EVEN\n\n")

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
    is_even = number % 2 == 0
    if is_even == True:
        print("Your number is even")
    else:
        print("Your number is odd")