import random

def ask_for_input():
    while True:
        guess = input("Please guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    return guess

def check_guess(guess, word):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

if __name__ == "__main__":
    word_list = ["apple", "banana", "pears", "grapes", "watermelon"]
    word = random.choice(word_list)
    while True:
        guess = ask_for_input()
        if check_guess(guess, word):
            break
    