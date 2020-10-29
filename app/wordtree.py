import time
import io
from app.config import Config


class WTNode:
    def __init__(self, string):
        self.data = string
        self.isWord = False
        self.void = False
        self.children = {}

    # def __repr__(self):
    #     repr = f"{{{self.data}: ["
    #     for child in self.children:
    #         repr += child
    #     return repr + "]}}"


class WordTree:
    def __init__(self):
        self.children = {}
        self.voided_nodes = set()
        self.voided_words = set()

    def __str__(self):
        return str(self.children)

    def add(self, word):
        """
        Adds the string word to the tree
        Originally used recursion, but more performance attained using while loop

        :param word:
        :param node:
        :return:
        """
        length = len(word)
        if length >= Config.MIN_WORD_SIZE:
            node = self  # initialise to root of tree
            letter_index = 0

            while letter_index < length:  # Loop through letters
                letter = word[letter_index]  # Set letter to next char in word

                if letter == "Q":
                    letter = "QU"
                    letter_index += 1

                letter_index += 1  # Increment letter_index (also used as loop counter)

                if letter not in node.children:  # If no child node exists for next letter
                    node.children[letter] = WTNode(letter)  # Create new node with next letter

                node = node.children[letter]  # Move to next node

            node.isWord = True  # Set isWord, indicating end of word in WordTree

    def find(self, word):
        length = len(word)
        if length >= Config.MIN_WORD_SIZE:
            node = self
            letter_index = 0

            while letter_index < length:  # Loop through remaining letters
                letter = word[letter_index]  # Set letter to next char in word

                if letter == "Q":
                    letter = "QU"
                    letter_index += 1

                letter_index += 1  # Increment letter_index (also used as loop counter)

                if letter not in node.children:  # If no child node exists for next letter
                    return False

                node = node.children[letter]  # Move to next node

            return node.isWord  # If isWord, indicates end of a valid word

        return True  # prevent words that are under min lenght being returned as problems

    def reset_tree(self):
        """
        THIS FUNCTION DOES NOT DELETE WORDS OR NODES FROM THE WORDTREE

        Resets VOIDed nodes and words (words that were set to isWord=False for optimisation purposes in )
        :return:
        """
        for node in self.voided_nodes:
            node.void = False
        self.voided_nodes = set()

        for node in self.voided_words:
            node.isWord = True
        self.voided_words = set()

    def build_wordtree(self, min_word_size=None):
        if min_word_size is not None:
            Config.MIN_WORD_SIZE = min_word_size

        start = time.time()

        with open(Config.DICTIONARY_ADDRESS, encoding="utf8") as file:
            for word in file.read().split("\n"):
                self.add(word)

        end = time.time()

        print(f"WordTree created in {end - start:.{Config.PRECISION}f}s")

        return self


wt = WordTree().build_wordtree()
