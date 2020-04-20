import random
import time

from app.board import Board
from app.config import Config
from app.wordtree import WordTree, WTNode
from app import create_app

moves = ["right",
         "left",
         "up",
         "down",
         "upRight",
         "upLeft",
         "downRight",
         "downLeft"]


def generate_valid_words(board):
    valid_words = []
    b = Board(board)
    print(b)

    boardSize = 4
    for i in range(boardSize):
        for j in range(boardSize):
            start_node = b.nodes[i][j]
            if start_node.letter in wt.children:
                valid_words += rec_words(start_node, wt.children[start_node.letter])

    return set(valid_words)


def rec_words(node, wt_node: WTNode, word="", visited=None):
    if visited is None:
        visited = []

    valid_words = []
    dict_letter = wt_node.data
    curr_word = word + dict_letter

    if wt_node.isWord:
        valid_words.append(curr_word)

    legal_trans = node.possible_transitions()

    for move in moves:
        if move in legal_trans:
            if node.transitions[move] not in visited:
                next_node = node.transitions[move]
                next_letter = next_node.letter
                if next_letter in wt_node.children:
                    valid_words.extend(rec_words(next_node, wt_node.children[next_letter], curr_word, visited + [node]))

    return valid_words


def create_wordtree(word_list, min_word_size=3):
    word_dictionary = WordTree()

    for word in word_list:
        if len(word) < min_word_size:
            continue
        word_dictionary.add(word)
    return word_dictionary


def build_word_dictionary(min_word_size=3):
    start = time.time()
    wt = WordTree()
    words = []

    with open(Config.DICTIONARY_ADDRESS, encoding="utf8") as file:
        for word in file.read().split("\n"):
            wt.add(word)
            # words.append(word)
    print(f"took {time.time() - start:.6f}s to create the word tree")

    return wt


wt = build_word_dictionary()

if __name__ == '__main__':
    from app.models import BoggleBoard

    def run_generator(board):
        start = time.time()
        word_list = generate_valid_words(board.generate_board())
        end = time.time()

        print(sorted(word_list))

        print(f"{len(word_list)} words were generated in {end - start:.6f} seconds")


    with create_app().app_context():
        print("\nPreconfigured board:")
        print("-" * 20)
        run_generator(BoggleBoard("LOPGPOCIHBIEGKLS"))

        run_generator(BoggleBoard("QuEENPOCIHBIEGKLS"))

        print("\nRandom board:")
        print("-" * 20)
        run_generator(BoggleBoard())


    def checkWordTree(wordList, wordTree):
        print("checking wordtree")
        missed_words = []
        for word in wordList:
            if not wordTree.findString(word):
                missed_words.append(word)
        print("finished checking wordtree")
        print(len(missed_words), " words were skipped:\n", missed_words)

    # checkWordTree(words, wt)
