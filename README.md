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

# Milestone 4
The following code is written for the Milestone 4 for the Hangman project.

```python
import random

class HangMan:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            first_idx = -1 
            for letter in self.word:
                if letter == guess:
                    idx = self.word.index(guess, first_idx + 1) 
                    self.word_guessed[idx] = guess
                    first_idx = idx
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    
    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) > 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetic character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

    if __name__ == "__main__":
    hangman = HangMan(["apple", "grapes"])
    hangman.ask_for_input()
```
The `HangMan` class has the following attributes:
* `word_list` = list of words for the game.
* `num_lives` = number of lives a player gets to play the game.
* `word` = random word from the word_list
* `word_guessed` = words guessed from the word in their corresponding position.
* `num_letters` = the unique number of letters in the word.
* `list_of_guesses` = the list of guesses the player has taken.

The `HangMan` class must be initialised with two parameters: `word_list` and `num_lives`. `word_list` is required, whereas, `num_lives` is optional with a default value of 5. Like follows: 
```python
# Initialise the game with default lives
hangman = HangMan(["apple", "bananas", "pears"])
# OR Initialise game with 10 lives.
hangman = HangMan(["apple", "bananas", "pears"], 10)
```

There are two methods available for the class. The `check_guess` method takes an argument `guess` and checks if the guess letter is present in `self.word` and updates the related attributes. The `ask_for_input` method asks the player for input, validates the input and starts the game. To run the game:
```markdown
First clone the project. navigate to the root directory of the project and run the command `python3 milestone_4.py`.
```