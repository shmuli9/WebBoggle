class Node:
    def __init__(self, letter, trans=None):
        self.letter = ""
        self.transitions = {
            "up": {},
            "down": {},
            "right": {},
            "left": {},
            "upRight": {},
            "upLeft": {},
            "downRight": {},
            "downLeft": {}
        }

        self.letter = letter
        if trans:
            for t in trans:
                self.transitions[t] = trans[t]

    def __str__(self):
        return f"Letter: {self.letter}"

    def add_transitions(self, trans):
        # print("Adding trans")
        # print(trans)
        for t in trans:
            self.transitions[t] = trans[t]
        # print(self.possible_transitions())

    def possible_transitions(self):
        trans = []
        for t in self.transitions:
            if self.transitions[t] != {}:
                trans.append(t)
        return trans


import random


class Board:
    size = 4
    nodes = [[{} for i in range(4)] for j in range(4)]

    def __str__(self):
        out = ""
        for i in range(self.size):
            for j in range(self.size):
                out += f"{str(self.nodes[i][j].letter)} " \
                       f"- Possible transitions: {str(self.nodes[i][j].possible_transitions())}"
                out += " " if j is not self.size - 1 else ""
            out += "\n" if i is not self.size - 1 else ""
        return out

    def __init__(self, board, size=4):
        self.size = size
        for i in range(size):
            for j in range(size):
                self.nodes[i][j] = Node(board[i][j])

        for i in range(size):
            canUp = i != 0
            canDown = i != 3
            for j in range(size):
                canLeft = j != 0
                canRight = j != 3

                trans = {
                    "up": self.nodes[i - 1][j] if canUp else {},
                    "down": self.nodes[i + 1][j] if canDown else {},
                    "right": self.nodes[i][j + 1] if canRight else {},
                    "left": self.nodes[i][j - 1] if canLeft else {},
                    "upRight": self.nodes[i - 1][j + 1] if canUp and canRight else {},
                    "upLeft": self.nodes[i - 1][j - 1] if canUp and canLeft else {},
                    "downRight": self.nodes[i + 1][j + 1] if canDown and canRight else {},
                    "downLeft": self.nodes[i + 1][j - 1] if canDown and canLeft else {}
                }

                self.nodes[i][j].add_transitions(trans)
