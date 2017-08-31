import random

# draw guessed letters and strikes
# print out win/lose


# create a list of words

# draw blank spaces for letters
def blank_word(str):
    blank_str = ''
    for l in str:
        blank_str += '*'
    print(blank_str)  # for testing
    return blank_str

# replace blanks with letters
def build_word(str, g, str_2)

        str_2.replace('*', g)
        return str_2


# guess loop
def guess_loop(new_str):
    # variables
    letter_guess = '1'
    player_word = blank_word(new_str)
    guess_list = []

    while player_word != new_str and len(guess_list) != 10:
        print(new_str)  # for testing
        print('\nYour Word: {}'.format(player_word))
        print('Guessed letters {}:'.format(guess_list))
        letter_guess = input('What letter would you like to guess? '
                             'You have {} guesses left: '
                             .format(10 - len(guess_list)))
        letter_guess = letter_guess.upper()
        if letter_guess in new_str:
            print(letter_guess)
            player_word = build_word(new_str, letter,guess, player_word)
       else:
            print('"{}" is not in the word.'.format(letter_guess))
            guess_list.append(letter_guess)

        # return word with letter(s) added in


def main():
    guess_loop(random.choice(word_list))




if __name__ == '__main__':
    main()
