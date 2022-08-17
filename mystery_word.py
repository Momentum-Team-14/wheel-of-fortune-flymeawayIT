from operator import truediv
import random


def play_game():
    name = input("What is your name?")
    wanna_play = input("Do you want to play a game ? (Y/N): ").upper()
    if wanna_play == "Y":
        print("Good Luck ! ", name)
        print("Guess a letter to try to guess the word; you get 8 guesses!")
    elif wanna_play == "Y":
        print("OK, Bye", name)
    with open('words.txt', 'r') as input_file:
        words = input_file.read()
    words_list = words.split()
    # #choose a random word from the list
    correct_word = random.choice(words_list)
    # make blank spaces
    length = (len(correct_word)*"_")
    # set counter for guess attempts
    # attempts = 0
    # set list for letters user has already guessed
    # letters_guessed = []
    print("Your word is", len(correct_word), "letters long")

    # with open('words.txt', 'r') as file:
    #     correct_word = file.read().replace('\n', "")
    right_list = []
    wrong_list = []

    guess_letters(correct_word, right_list, wrong_list) 


def guess_letters(word, right_list, wrong_list):
    letters_in_correct_word = ["_" for letter in word]
    tries = 8
    while tries:
        guess = input("Guess your first letter now - ").lower()
        if guess not in word:
            tries -= 1
            wrong_list.append(guess_letters)
            print(f'Wrong, you have {tries} more tries')
        else:
            for i in range(len(letters_in_correct_word)):
                if guess == word[i]:
                    letters_in_correct_word[i] = guess
                    right_list.append(guess_letters)
            print(letters_in_correct_word)


if __name__ == "__main__":
    play_game()