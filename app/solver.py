import time

from board import Board
from wordtree import WordTree, WTNode

from app.config import Config

moves = {"right", "left", "up", "down", "upRight", "upLeft", "downRight", "downLeft"}


def generate_valid_words(board):
    valid_words = []
    # print(board)

    boardSize = 4
    for i in range(boardSize):
        for j in range(boardSize):
            start_node = board.nodes[i][j]
            if start_node.letter in wt.children:
                valid_words += rec_words(start_node, wt.children[start_node.letter], visited={})

    # withD = len(valid_words)
    # print(sorted(valid_words))
    # withOD = len(set(valid_words))
    # diff = withD - withOD
    # print(f"{diff},{diff / withD * 100: .2f}, {withD}")
    # print("Number of duplicates", diff)
    # print(f"%age duplicates {diff / withD * 100: .2f}%")
    return valid_words


def rec_words(node, wt_node: WTNode, word="", visited=None):
    valid_words = []
    curr_word = word + wt_node.data

    if wt_node.isWord:  # word has been found in wordtree matching the boggle word
        valid_words.append(curr_word)
        wt_node.isWord = False  # mark as non word to prevent duplication
        wt.voided_words.append(wt_node)
        void_this_node = True
        for child in wt_node.children:
            if not wt_node.children[child].void:
                void_this_node = False
                break
        if void_this_node:
            wt_node.void = True  # no unvoided children so void
            wt.voided_nodes.append(wt_node)  # save to unvoid for reuse of wordtree dictionary
    legal_trans = node.possible_transitions()

    for move in moves.intersection(legal_trans):  # loop through all legal moves
        next_node = node.transitions[move]
        if next_node not in visited:
            next_letter = next_node.letter
            if next_letter in wt_node.children:
                next_wt_node = wt_node.children[next_letter]
                if not next_wt_node.void:
                    new_visited = set(visited)  # copy values to new variable
                    new_visited.add(node)  # add current node to visited
                    valid_words.extend(
                        rec_words(next_node, next_wt_node, curr_word, new_visited))

    # check if wt node has unvoided children, if it does not, then void the node
    for child in wt_node.children:
        if not wt_node.children[child].void:
            return valid_words  # early return, as one or more children are not void
    wt_node.void = True  # no unvoided children so void
    wt.voided_nodes.append(wt_node)
    return valid_words


def build_word_dictionary(min_word_size=3):
    start = time.time()
    wt = WordTree()

    with open(Config.DICTIONARY_ADDRESS, encoding="utf8") as file:
        for word in file.read().split("\n"):
            wt.add(word)
    end = time.time()
    print(f"took {end - start:.6f}s to create the WordTree")

    return wt


if __name__ == '__main__':

    global wt
    wt = build_word_dictionary()


    def run_generator(board):
        start = time.time()
        word_list = generate_valid_words(board)
        end = time.time()

        print(sorted(word_list))

        print(f"{len(word_list)} words were generated in {end - start:.6f} seconds")


    # with create_app().app_context():
    #     print("\nPreconfigured board:")
    #     print("-" * 20)
    #     run_generator(Board("LOPGPOCIHBIEGKLS"))
    #
    #     # run_generator(Board("QuEENPOCIHBIEGKLS"))
    #
    #     print("\nRandom boards:")
    #     print("-" * 20)
    #     for _ in range(1):
    #         run_generator(Board())

    def test_suite(num_runs=10):

        def avg(numbers):
            total = 0
            for el in numbers:
                total += el
            return total / len(numbers)

        dice = ["QuEENPOCIHBIEGKLS", "LOPGPOCIHBIEGKLS"]
        #  dice[0] if run % 2 == 0 else dice[1]

        run_times = []
        global duplicates
        for run in range(num_runs):
            wt.fixVoids()
            start = time.time()
            word_list = generate_valid_words(Board(dice[1]))
            end = time.time()
            del word_list
            run_times.append(end - start)
            del start, end

        precision = 6
        print(
            f"average run time over {num_runs} random boards was: {avg(run_times):.{precision}f}s (total:{sum(run_times):.{precision}f}s)")
        print(f"max run time was {max(run_times):.{precision}f}s")
        print(f"min run time was {min(run_times)}s")
        print(f"delta (max - min) run time was {max(run_times) - min(run_times):.{precision}f}s")
        print(run_times[:1000])


    test_suite(10000)


def checkWordTree(wordList, wordTree):
    print("checking wordtree")
    missed_words = []
    for word in wordList:
        if not wordTree.findString(word):
            missed_words.append(word)
    print("finished checking wordtree")
    print(len(missed_words), " words were skipped:\n", missed_words)

# checkWordTree(words, wt)
