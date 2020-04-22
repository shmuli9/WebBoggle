import time

from app.config import Config


class WTNode:
    def __init__(self, string):
        self.data = string
        self.isWord = False
        self.void = False
        self.children = {}


class WordTree:
    def __init__(self):
        self.children = {}
        self.voided_nodes = set()
        self.voided_words = set()

    def __str__(self):
        return str(self.children)

    def addToBranch(self, st, node):
        i = 0
        while i < len(st):
            if i == len(st) - 1:
                node.isWord = True
                return
            letter = st[i]

            if letter == "Q":
                letter = "Qu"
                i += 1
            i += 1

            if letter not in node.children:
                newNode = WTNode(letter)
                node.children[letter] = newNode
            node = node.children[letter]

        # if not st:  # base case, string is empty
        #     node.isWord = True
        #     return
        #
        # chars = st[0]
        # remaining = st[1:]
        # if chars == "Q":
        #     chars = "Qu"
        #     remaining = st[2:]
        #
        # if chars not in node.children:
        #     newNode = WTNode(chars, None)
        #     node.children[chars] = newNode
        # return self.addToBranch(remaining, node.children[chars])

    # adds the string st in the tree
    def add(self, st):
        l = len(st)
        if l > 2:  # min word size is 3
            i = 0
            letter = st[0]
            i += 1
            if letter == "Q":
                letter = "Qu"
                i += 1
            if letter not in self.children:
                self.children[letter] = WTNode(letter)
            node = self.children[letter]

            while i < l:  # loop through remaining
                letter = st[i]
                if letter == "Q":
                    letter = "Qu"
                    i += 1
                i += 1

                if letter not in node.children:
                    node.children[letter] = WTNode(letter)
                node = node.children[letter]
            node.isWord = True  # final node is a word

        # if len(st) > 2:
        #     chars = st[0]
        #     remaining = st[1:]
        #     if chars == "Q":
        #         chars = "Qu"
        #         remaining = st[2:]
        #     if chars not in self.children:
        #         newNode = WTNode(chars, None)
        #         self.children[chars] = newNode
        #     self.addToBranch(remaining, self.children[chars])

    def _findString(self, st, node):
        if not st:  # base case, string is empty or node is empty
            if node:  # return multiplicity
                return node.isWord
            return False

        chars = st[0]
        remaining = st[1:]
        if chars == "Q":
            chars = "Qu"
            remaining = st[2:]

        if chars in node.children:
            return self._findString(remaining, node.children[chars])
        return False

    def findString(self, st):
        chars = st[0]
        remaining = st[1:]
        if chars == "Q":
            chars = "Qu"
            remaining = st[2:]

        if chars not in self.children:  # or (chars in self.children and self.children[chars].void)
            return False
        return self._findString(remaining, self.children[chars])

    def deleteWord(self, st):
        chars = st[0]
        remaining = st[1:]
        if chars == "Q":
            chars = "Qu"
            remaining = st[2:]

        if chars not in self.children:
            return
        return self._deleteWord(remaining, self.children[chars], self)

    def _deleteWord(self, st, node: WTNode, parentNode):
        if not st:  # empty string, indicates at end of word
            if node.isWord:
                node.isWord = False
                self.voided_nodes.append(node)
            return

        chars = st[0]
        remaining = st[1:]
        if chars == "Q":
            chars = "Qu"
            remaining = st[2:]

        if chars in node.children:
            self._deleteWord(remaining, node.children[chars], node)
        if not node.children:  # node has no child so safe to void it
            if node.isWord:
                node.isWord = False
                self.voided_nodes.append(node)
        return

    # Resets voided nodes and words (words that were set to isWord=False)
    def resetTree(self):
        for node in self.voided_nodes:
            node.void = False
        self.voided_nodes = set()
        for node in self.voided_words:
            node.isWord = True
        self.voided_words = set()

    def build_wordtree(self, min_word_size=3):
        start = time.time()

        with open(Config.DICTIONARY_ADDRESS, encoding="utf8") as file:
            for word in file.read().split("\n"):
                l = len(word)
                if l > min_word_size - 1:  # min word size is 3
                    i = 0
                    letter = word[0]
                    i += 1
                    if letter == "Q":
                        letter = "Qu"
                        i += 1
                    if letter not in self.children:
                        self.children[letter] = WTNode(letter)
                    node = self.children[letter]

                    while i < l:  # loop through remaining
                        letter = word[i]
                        if letter == "Q":
                            letter = "Qu"
                            i += 1
                        i += 1

                        if letter not in node.children:
                            node.children[letter] = WTNode(letter)
                        node = node.children[letter]
                    node.isWord = True  # final node is a word
        end = time.time()
        print(f"took {end - start:.6f}s to create the WordTree")

        return self


wt = WordTree().build_wordtree()

# wt = WordTree()
# test_words = ["cart",
#               "art",
#               "car",
#               "cccc",
#               "Queen",
#               "Que",
#               "AQu"]
# for word in test_words:
#     wt.add(word)
# print(wt)
#
# print(str(wt.findString("cart")))
# wt.deleteWord("cart")
# print(str(wt.findString("cart")))
#
# print(wt)
#
# for word in test_words:
#     wt.deleteWord(word)
#
# print(wt)
# print(str(wt.findString("AQu")))
