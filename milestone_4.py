import random

class HangMan:
    """
    This is the docstring for the HangMan class.

    Hangman class is a class the initialises a hangman game.

    Attributes:
        word_list (list[str]): a list of words for the game.
        num_lives (int): number of lives for the player of the game. Default is 5.
        word (str): a random word for the game from the word_list.
        word_guesses (list[str]): list of empty string for each character in word.
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
        self.word_guesses = ['' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
