import random


def game(total_tries, min, max):

    """runs number guess game loop"""
    n = random.randint(min, max)
    guess = ""  # empty variable for player guess
    guesses = []

    while len(guesses) < total_tries and guess != n:

        # get guess & catch errors
        try:
            guess = int(input(
                        "Guess a number {} - {}, you have {} tries left."
                        "\nNumbers guessed {}: "
                        .format(min, max, total_tries - len(guesses),
                                guesses)))
            print("\n")  # force a line break for ease of reading
        except ValueError:
            print("\nThat's not a valid number!")

        else:
            # validate guess in range
            if guess < min or guess > max:
                print("That guess isn't in the acceptable range!")

            # compare guess
            elif guess == n:
                print("Correct. You guessed in {} tries. Way to be awesome."
                      .format(len(guesses)))
            elif len(guesses) >= total_tries:
                print("You ran out of guesses. The correct answer was {}."
                      .format(n))
            else:
                guesses.append(guess)
                if guess > n:
                    print("Sorry, guess lower.")
                else:
                    print("Sorry, guess higher.")

    # play again?
    again = input("Press any key to play again or type 'Q' to quit: ")
    if again != 'Q':
        main()
    else:
        print("Thanks for playing")


def main():
    game(10, 1, 100)


if __name__ == '__main__':
    main()
