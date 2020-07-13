print("This program tests a number to check if it is a MERSENNE PRIME\n\n")

while True:
    number = input("Please input the number you would like to test: ")
    number = int(number)
    try:
        number = int(number)
    except ValueError:
        print("Please input a valid number.")
        continue
    if number < 0:
        print("Please input a positive number")
        continue
    if number < 3:
        print("The lowest Mersenne Prime number is 3.")
        continue

    if number == 3:
        print("Your number is a Mersenne Prime.")
        continue

    if number == 7:
        print("Your number is a Mersenne Prime.")
        continue

    if number == 31:
        print("Your number is a Mersenne Prime.")
        continue

    while True:
        c = 0
        for n in range(1, number + 1):
            if number % n == 0:
                c += 1
        is_prime = c == 2

        if is_prime == False or number <= 126:
            print("Your number is not a Mersenne Prime.")
            break

        number += 1
        while number % 2 == 0:
            number = number / 2

        if number == 1:
            print("Your number is a Mersenne Prime.")
            break
        else:
            print("Your number is not a Mersenne Prime.")
            break