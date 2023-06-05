# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Milestone 2
The following is the code written for Milestone 2 of the Hangman project

```python
import random

word_list = ["apple", "pear", "banana", "watermelon", "grapes"]
word = random.choice(word_list)
guess = input("Please enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
print(word)
```

The `word_list` variable stores my five favourite fruits in a list. The `word` variable generates a random fruit from the list of fruits and stores it. The `guess` variable stores a single letter that the user has entered. The `if and else conditionals` checks if the user has entered correct value, i.e. if the entered letter is equal to length 1 and is alphabetic. Then correct print statements are printed. Finally, the random word chosen from the `word_list` variable is printed.

# Milestone 3
The following code is written for Milestone 3 of the Hangman project

```python
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
    guess = ask_for_input()
    check_guess(guess, word) 
```

The `ask_for_input` function asks the user to enter a letter, validates it and returns the letter. The `check_guess` function takes in two parameters, `guess` and `word` and checks if the guess letter is in the word and prints the correct statement. In the `main` of the program, first a `word_list` variable is defined with five fruits. A random fruit is then assigned to the `word` variable. Then the `ask_for_input` function is called and the return value assigned to the `guess` variable. Finally, `check_guess` function is called with `guess` and `word` variable passed as arguments.