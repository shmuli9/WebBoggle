import random
import time

from app import BoggleBoard
from board import Board
from config import Config
from wordtree import WordTree, WTNode

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

    # if curr_word.upper() in words:
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


if __name__ == '__main__':
    def generate_board(dice=None):
        if not dice:
            board_dice = random.sample(Config.DICE, len(Config.DICE))

            board = []
            for _ in range(4):
                board.append([random.choice(board_dice.pop()) for __ in range(4)])

        else:
            board = [[dice[i + j] for j in range(4)] for i in range(4)]

        return BoggleBoard(board)


    def run_generator(board):
        start = time.time()
        word_list = generate_valid_words(generate_board().board)
        end = time.time()

        print(sorted(word_list))

        print(f"{len(word_list)} words were generated in {end - start:.6f} seconds")

    start = time.time()
    wt = WordTree()
    words = []
    with open("words_alpha_collins.txt") as file:
        for word in file.read().split("\n"):
            wt.add(word)
            # words.append(word)
    print(f"took {time.time() - start:.6f}s to create the word tree")

    print("\nPreconfigured board:")
    print("-" * 20)
    run_generator(generate_board("LOPGPOCIHBIEGKLS"))

    print("\nRandom board:")
    print("-" * 20)
    run_generator(generate_board())

    def checkWordTree(wordList, wordTree):
        print("checking wordtree")
        missed_words = []
        for word in wordList:
            if not wordTree.findString(word):
                missed_words.append(word)
        print("finished checking wordtree")
        print(len(missed_words), " words were skipped:\n", missed_words)

    # checkWordTree(words, wt)
