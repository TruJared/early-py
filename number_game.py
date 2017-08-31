import random
again = 1


def main(min, max):
    number = random.randint(min, max)
    tries = 0
    guess = 0
    while True:
        tries += 1
        # get guess & catch errors
        try:
            guess = int(input("Guess a number {} - {}: ".format(min, max)))
        except ValueError:
            print("That's not a valid number!")
            tries -= 1
            continue
        # compare guess
        if guess == number:
            print("Correct. You guessed in {} tries. Way to be awesome."
                  .format(tries))
            break
        elif tries >= 10:
            print("You ran out of guesses. The correct answer was {}."
                  .format(number))
            break
        else:
            if guess > number:
                print("Sorry, guess lower.")
            else:
                print("Sorry, guess higher.")


while again != 'Q':
    again = input("Press any key to play again or type 'Q' to quit: ")
    if again != 'Q':
        tries = 0
        if __name__ == '__main__':
            main(1, 10)
    else:
        print("Thanks for playing!")
