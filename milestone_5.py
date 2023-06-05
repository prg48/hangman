import random

class HangMan:
    """
    This is the docstring for the HangMan class.

    Hangman class is a class the initialises a hangman game.

    Attributes:
        word_list (list[str]): a list of words for the game.
        num_lives (int): number of lives for the player of the game. Default is 5.
        word (str): a random word for the game from the word_list.
        word_guessed (list[str]): list of letters of guessed word by the player. Initially a list of empty chars the length of the word.
        num_letters (int): number of unique characters in word
        list_of_guesses (list[char]): list that holds the guesses of characters a player makes. Initially is [].
    """
    def __init__(self, word_list, num_lives=5):
        """
        Constructor for the HangMan class.

        Parameters:
            word_list (list[str]): a list of words for the instance of the game.
            num_lives (int): number of lives a player gets for the instance of the game. Default is 5.
        """
        self.word = random.choice(word_list)
        self.word_guessed = ['' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        This method checks if the guess is in the word

        Args:
            guess (char): a letter guess.
        """
        guess = guess.lower()
        self.list_of_guesses.append(guess)
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            first_idx = -1 # int to start searching for the index of guess in word
            for letter in self.word:
                if letter == guess:
                    idx = self.word.index(guess, first_idx + 1) # check for the index of guess in word
                    self.word_guessed[idx] = guess
                    first_idx = idx
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    
    def ask_for_input(self):
        """
        This method asks for input from the player and checks guesses.
        """
        guess = input("Please guess a letter: ")
        if len(guess) > 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetic character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)

def play_game(word_list):
    """
    This method initialises the hangman game and starts the play loop

    Args:
        word_list (lst[str]): The list of words for the game
    """
    num_lives = 5
    game = HangMan(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break

if __name__ == "__main__":
    play_game(["apple", "grape"])
