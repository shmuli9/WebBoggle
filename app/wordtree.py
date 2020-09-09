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

    # def addToBranch(self, st, node):
    #     if not st:  # base case, string is empty
    #         node.isWord = True
    #         return
    #
    #     chars = st[0]
    #     remaining = st[1:]
    #     if chars == "Q":
    #         chars = "Qu"
    #         remaining = st[2:]
    #
    #     if chars not in node.children:
    #         newNode = WTNode(chars, None)
    #         node.children[chars] = newNode
    #     return self.addToBranch(remaining, node.children[chars])
    #
    #
    # def add(self, st):
    #     '''
    #     Adds the string st to the tree using recursive algorithm
    #
    #     :param st:
    #     :return:
    #     '''
    #     if len(st) > 2:
    #         chars = st[0]
    #         remaining = st[1:]
    #         if chars == "Q":
    #             chars = "Qu"
    #             remaining = st[2:]
    #         if chars not in self.children:
    #             newNode = WTNode(chars, None)
    #             self.children[chars] = newNode
    #         self.addToBranch(remaining, self.children[chars])
    # def add(self, st):
    #     """
    #     Adds the string st to the tree
    #     Originally used recursion, but more performance attained using while loop
    #     See commented out code above...
    #
    #     :param st:
    #     :return:
    #     """
    #     l = len(st)
    #     if l > 2:  # min word size is 3
    #         i = 0
    #         letter = st[0]
    #         i += 1
    #         if letter == "Q":
    #             letter = "Qu"
    #             i += 1
    #         if letter not in self.children:
    #             self.children[letter] = WTNode(letter)
    #         node = self.children[letter]
    #
    #         while i < l:  # loop through remaining
    #             letter = st[i]
    #             if letter == "Q":
    #                 letter = "Qu"
    #                 i += 1
    #             i += 1
    #
    #             if letter not in node.children:
    #                 node.children[letter] = WTNode(letter)
    #             node = node.children[letter]
    #         node.isWord = True  # final node is a word

    # Resets voided nodes and words (words that were set to isWord=False)
    def resetTree(self):
        for node in self.voided_nodes:
            node.void = False
        self.voided_nodes = set()
        for node in self.voided_words:
            node.isWord = True
        self.voided_words = set()

    def build_wordtree(self, min_word_size=None):
        if min_word_size is None:
            min_word_size = Config.MIN_WORD_SIZE

        start = time.time()

        with open(Config.DICTIONARY_ADDRESS, encoding="utf8") as file:
            for word in file.read().split("\n"):
                # originally self.add function was called here 290,000+ times per application run
                # for perf, function code was added here
                length = len(word)
                if length >= min_word_size:
                    letter = word[0]
                    letter_index = 1
                    if letter == "Q":  # Q replacement, as QU is what appears on Boggle dice
                        letter = "QU"
                        letter_index += 1  # Boggle dictionary used as source, so all Q's followed by U
                    if letter not in self.children:  # If no child (word) starts with current letter
                        self.children[letter] = WTNode(letter)  # Add the node with value of letter to WordTree children
                    node = self.children[letter]  # Initialise node to the correct WordTree child

                    while letter_index < length:  # Loop through remaining letters
                        letter = word[letter_index]  # Set letter to next char in word
                        if letter == "Q":
                            letter = "QU"
                            letter_index += 1
                        letter_index += 1  # Increment letter_index (also used as loop counter)

                        if letter not in node.children:  # If no child node exists for next letter
                            node.children[letter] = WTNode(letter)  # Create new node with next letter
                        node = node.children[letter]  # Move to next node
                    node.isWord = True  # Set isWord, indicating end of word in WordTree
        end = time.time()
        print(f"WordTree created in {end - start:.{Config.PRECISION}f}s")

        return self


wt = WordTree().build_wordtree()
