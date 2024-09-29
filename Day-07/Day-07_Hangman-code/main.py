import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_random = random.choice(word_list)

placeholder = ["_" for _ in chosen_random]
print(''.join(placeholder))

game_over = False

check = []

while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()

    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    for position in range(len(chosen_random)):
        if chosen_random[position] == guess:
            placeholder[position] = guess
    print(''.join(placeholder))

    if "_" not in placeholder:
        print("You win!")

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
    #  is, "Wrong" if it's not.