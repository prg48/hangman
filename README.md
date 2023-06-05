# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Milestone 1
The following is the code written for Milestone 1 of the Hangman project

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