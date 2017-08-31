import statistics

# variables
min = 1
max = 100
tries = 10


def guess_formula(min, max):
    """formula to calculate guess (always median)"""
    num_list = [min, max]
    guess = int(statistics.median(num_list))
    return guess


def game(n, min, max):
    guess = 0
    guesses = []
    max += 1  # adjusts parameters in case user picks highest int

    while len(guesses) < tries and guess != n:
        """game loop"""
        guess = guess_formula(min, max)
        guesses.append(guess)
        print("\nMy guess is {}.".format(guess))

        # is guess correct?
        if guess == n:
            print("I win sucka'")
        else:
            hi_lo = int(input("Is your number higher or lower"
                        "\nPress 1 for lower, 2 for higher: "))

            # adjust formula for higher or lower
            if hi_lo == 2:
                min = guess
            else:
                max = guess

    # results loop
    if len(guesses) >= tries:
        print("How could this be... you won???")
    print("Good-bye")


def main():
    print("Think of a number between {} and {}.".format(min, max))
    try:
        n = int(input("What is your number? "))
    except ValueError:
        print("Not a valid number.")
        main()

    if n >= min and n <= max:
        game(n, min, max)
    else:
        print("Your number is not in the valid range.")
        main()


if __name__ == '__main__':
    main()
