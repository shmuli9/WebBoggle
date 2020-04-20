import random
import time

from app import BoggleBoard
from board import Board
from config import Config
from wordtree import WordTree

moves = ["right",
         "left",
         "up",
         "down",
         "upRight",
         "upLeft",
         "downRight",
         "downLeft"]


def generate_valid_words(board, dictionary_words):
    valid_words = []
    b = Board(board)
    print(b)

    boardSize = 4
    for i in range(boardSize):
        for j in range(boardSize):
            start_node = b.nodes[i][j]
            valid_words += rec_words(start_node)

    return set(valid_words)


def rec_words(node, word="", visited=None):
    if visited is None:
        visited = []

    valid_words = []
    curr_word = word + node.letter

    if len(curr_word) > 2:  # min length of word is 3
        if curr_word.upper() in words: # if letter.isWord:
            valid_words.append(curr_word.upper())
        if len(curr_word) > 4:
            return valid_words

    trans = node.possible_transitions()

    for move in moves:
        if move in trans:
            if node.transitions[move] not in visited:
                valid_words.extend(rec_words(node.transitions[move], curr_word, visited + [node]))

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
        word_list = generate_valid_words(generate_board().board, words)
        end = time.time()

        print(sorted(word_list))

        print(f"{len(word_list)} words were generated in {end - start:.6f} seconds")

    # def checkWordTree(wordList, wordTree):
    #     print("checking wordtree")
    #     missed_words = []
    #     for word in wordList:
    #         if not wordTree.findString(word):
    #             missed_words.append(word)
    #     print("finished checking wordtree")
    #     print(len(missed_words), " words were skipped:\n", missed_words)

    # checkWordTree(words, wordsInTree)

    start = time.time()
    wt = WordTree()
    with open("words_alpha_collins.txt") as file:
        for word in file.read().split("\n"):
            wt.add(word)
    print(time.time() - start, "s")

    print("\nPreconfigured board:")
    print("-" * 20)
    run_generator(generate_board("LOPGPOCIHBIEGKLS"))

    print("\nRandom board:")
    print("-" * 20)
    run_generator(generate_board())
