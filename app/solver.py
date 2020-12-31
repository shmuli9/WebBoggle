from app.wordtree import WTNode


class Solver:
    def __init__(self):
        from app.wordtree import wt
        self.wt = wt

    def generate_words(self, board, duplicates=False):
        valid_words = {}

        for i in range(board.size):
            for j in range(board.size):
                start_bg_node = board.nodes[i][j]
                start_wt_node = self.wt.children[start_bg_node.letter]

                valid_words.update(self.find_words(start_bg_node, start_wt_node))

        if duplicates:
            duplicates_analysis(valid_words)

        # cleanup
        self.wt.reset_tree()

        return valid_words

    def find_words(self, bg_node, wt_node: WTNode, word="", visited={}):
        """
        :param bg_node: Boggle board node
        :param wt_node: WordTree node
        :param word: current state of word being found
        :param visited: set of previously visited Boggle board nodes
        :return: list of found words
        """

        valid_words = {}
        curr_word = word + wt_node.data

        if wt_node.isWord:  # word has been found in wordtree matching the boggle word
            valid_words[curr_word] = [bg_node.coords] + [n.coords for n in visited]

            wt_node.isWord = False  # mark as non word to prevent duplication
            self.wt.voided_words.add(wt_node)

            void_this_node = True  # initialise to True
            for child in wt_node.children:
                if not wt_node.children[child].void:
                    void_this_node = False  # set to False if voiding isn't relevant
                    break

            if void_this_node:  # no unvoided children
                wt_node.void = True
                self.wt.voided_nodes.add(wt_node)  # save to unvoid for reuse of wordtree dictionary

        for move in bg_node.transitions:  # loop through all legal moves
            if bg_node.transitions[move] not in visited:
                next_node = bg_node.transitions[move]

                if next_node.letter in wt_node.children:
                    if not wt_node.children[next_node.letter].void:
                        new_visited = set(visited)  # copy values to new variable
                        new_visited.add(bg_node)  # add current node to visited
                        valid_words.update(
                            self.find_words(next_node, wt_node.children[next_node.letter], curr_word, new_visited))

        # check if wt node has unvoided children, if it does not, then void the node
        for child in wt_node.children:
            if not wt_node.children[child].void:
                return valid_words  # early return, as one or more children are not void

        wt_node.void = True  # no unvoided children so void
        self.wt.voided_nodes.add(wt_node)

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
