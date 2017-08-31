import random

word_list = ['hello']  # radom choice word list
wrong_guesses = []  # collects correct guesses
right_guesses = []  # collects wrong guesses


# reveal guessed letters in word to player
def revealed_word(guess, word):
    for letter in word:
        if letter in right_guesses:
            print(letter, end='')
        else:
            print('*', end='')

    # for testing
    print('right guesses {}'.format(right_guesses))
    print('wrong guesses {}'.format(wrong_guesses))


# collect guess
def player_loop(word):
    guess = input('\nPlease guess a letter? ').lower()

    # error catching
    if len(guess) != 1 or not guess.isalpha():
        print('You can only guess one letter!')
    elif guess in wrong_guesses or guess in right_guesses:
        print('You already guessed that letter!')

    # builds lists and calls revealed_word function
    else:
        if guess in word:

            # loop to append multiples of same letters for win condition
            for letter in word:
                if letter == guess:
                    right_guesses.append(guess)
        else:
            wrong_guesses.append(guess)

        revealed_word(guess, word)


# main loop
while True:
    word = random.choice(word_list)

    if len(right_guesses) == len(word):
        print('Congratulations you guessed the word')
    elif len(wrong_guesses) >= 7:
        print('Sorry, you ran out of tries.')
        print('The word was {}.'.format(word))
    else:
        player_loop(word)


if __name__ == '__main__':
    main()























