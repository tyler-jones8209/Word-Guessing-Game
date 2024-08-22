import random
def hangman():

    # open and read file in corresponding directory
    inputFile = open("HangmanWords.txt", "r")

    # parse through each word in the file and strip, make it uppercase, and add to list of words
    word_number = random.randint(0, 853)
    word_list = []
    for word in inputFile:
        word = word.strip()
        word = word.upper()
        word_list.append(word)
    # pick a random word from the list
    random_word = word_list[word_number]

    # make a blank list with the corresponding number of blank spaces as the word
    guess_list = []
    for x in range(0, len(list(random_word))):
        guess_list.append("_")

    # mistake counter and list that stores all wrong words
    mistake_count = 0
    mistake_list = []

    # list that will be compared to guess list until they match
    random_word_list = list(random_word)

    # starting the loop (game)
    print("Let's Play Hangman. Guess a Letter")
    while guess_list != random_word_list and mistake_count < 7:
        
        # print lives remaining, incorrect letters, and the progress of the correct word
        print("(" + str((7 - mistake_count)) + " Lives Remaining)")
        print("Wrong Guesses: " + " ".join(mistake_list))
        print(" ".join(guess_list))

        # taking user input and uppercasing it for simplicity
        guess = input("Guess: ")
        guess = guess.upper()

        # if input is not a letter OR more than one letter, it prompts you to try again
        if guess not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or len(guess) > 1:
            print("Please Enter a Single Letter")

        # if input is not in the answer and not already been guessed, you get a life taken away
        elif guess not in random_word and guess not in mistake_list:
            mistake_count += 1
            mistake_list.append(guess)

        # if input is not in the answer but IS in the mistake list, you are reminded rather than losing a life
        elif guess not in random_word and guess in mistake_list:
            print("You already tried " + guess)

        # if input is a correct letter, put the letter in the correct spot of the guess list
        # thankfully accounts for multiple occurences of the letter
        elif guess in random_word:
            indices = [index for index, value in enumerate(random_word_list) if value == guess]
            for index in indices:
                guess_list[index] = guess

    # loop breaks after 7 fails and you are shown the word
    if mistake_count == 7:
        print("You F A I L E D. The answer was " + random_word)

    # loop breaks after guessing the word correctly and you get a victory message
    elif mistake_count != 7:
        print("YOU DID IT!!! The answer was " + random_word)

    # close the file obviously
    inputFile.close()

hangman()
