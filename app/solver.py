from app.wordtree import WTNode, wt


class Solver:
    def __init__(self):
        self.wt = wt

    def generate_words(self, board, duplicates=False):
        valid_words = []

        for i in range(board.size):
            for j in range(board.size):
                start_node = board.nodes[i][j]

                valid_words += self.find_words(start_node, wt.children[start_node.letter], visited={})

        if duplicates:
            duplicates_analysis(valid_words)

        # cleanup
        wt.reset_tree()

        return valid_words

    def find_words(self, node, wt_node: WTNode, word="", visited=None):
        valid_words = []
        curr_word = word + wt_node.data

        if wt_node.isWord:  # word has been found in wordtree matching the boggle word
            valid_words.append(curr_word)
            wt_node.isWord = False  # mark as non word to prevent duplication
            wt.voided_words.add(wt_node)

            void_this_node = True  # initialise to True
            for child in wt_node.children:
                if not wt_node.children[child].void:
                    void_this_node = False  # set to False if voiding isn't relevant
                    break

            if void_this_node:  # no unvoided children
                wt_node.void = True
                wt.voided_nodes.add(wt_node)  # save to unvoid for reuse of wordtree dictionary

        for move in node.transitions:  # loop through all legal moves
            if node.transitions[move] not in visited:
                next_node = node.transitions[move]

                if next_node.letter in wt_node.children:
                    if not wt_node.children[next_node.letter].void:
                        new_visited = set(visited)  # copy values to new variable
                        new_visited.add(node)  # add current node to visited
                        valid_words.extend(
                            self.find_words(next_node, wt_node.children[next_node.letter], curr_word, new_visited))

        # check if wt node has unvoided children, if it does not, then void the node
        for child in wt_node.children:
            if not wt_node.children[child].void:
                return valid_words  # early return, as one or more children are not void

        wt_node.void = True  # no unvoided children so void
        wt.voided_nodes.add(wt_node)

        return valid_words

    @staticmethod
    def duplicates_analysis(valid_words):
        """
        Deprecated as current algorithm can't produce duplicate words
        :param valid_words:
        :return:
        """
        withD = len(valid_words)
        # print(sorted(valid_words))
        withOD = len(set(valid_words))  # use set() to remove duplicates
        diff = withD - withOD
        print(f"{diff},{diff / withD * 100: .2f}, {withD}")
        print("Number of duplicates", diff)
        print(f"%age duplicates {diff / withD * 100: .2f}%")

    def verify_wordtree(self):
        return self.wt.verify_wordtree()


solver = Solver()
