import random
import time

from app import BoggleBoard
from board import Board
from config import Config


def generate_valid_words(board, dictionary_words):
    valid_words = []
    b = Board(board)
    print(b)
    # print(b.print_board())

    for i in range(4):
        for j in range(4):
            start_node = b.nodes[i][j]
            valid_words += (rec_words("", dictionary_words, start_node, [], []))

    return valid_words


def rec_words(word, dictionary, node, visited, words):
    if visited is None:
        visited = []
    if node in visited:
        return words
    visited.append(node)
    curr_word = word + node.letter

    if curr_word.lower() in dictionary:
        words.append(curr_word.upper())

    # if len(curr_word) > 15:
    #     return words

    trans = node.possible_transitions()

    if "upLeft" in trans:
        return rec_words(curr_word, dictionary, node.transitions["upLeft"], visited, words)
    if "up" in trans:
        return rec_words(curr_word, dictionary, node.transitions["up"], visited, words)
    if "upRight" in trans:
        return rec_words(curr_word, dictionary, node.transitions["upRight"], visited, words)
    if "left" in trans:
        return rec_words(curr_word, dictionary, node.transitions["left"], visited, words)
    if "right" in trans:
        return rec_words(curr_word, dictionary, node.transitions["right"], visited, words)
    if "downLeft" in trans:
        return rec_words(curr_word, dictionary, node.transitions["downLeft"], visited, words)
    if "down" in trans:
        return rec_words(curr_word, dictionary, node.transitions["down"], visited, words)
    if "downRight" in trans:
        return rec_words(curr_word, dictionary, node.transitions["downRight"], visited, words)
    return words


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
        print(word_list)

        print(f"{len(word_list)} words were generated in {end - start:.6f} seconds")


    with open("words_alpha.txt") as file:
        words = file.read().split("\n")

    print("\nPreconfigured board:")
    print("-" * 20)
    run_generator(generate_board("LOPGPOCIHBIEGKLS"))

    print("\nRandom board:")
    print("-" * 20)
    run_generator(generate_board())
