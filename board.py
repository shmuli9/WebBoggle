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
    def __str__(self):
        out = ""
        for i in range(self.size):
            for j in range(self.size):
                out += f"{str(self.nodes[i][j].letter)} " \
                    # f"- Possible transitions: {str(self.nodes[i][j].possible_transitions())}"
                out += " " if j is not self.size - 1 else ""
            out += "\n" if i is not self.size - 1 else ""
        return out

    def print_board(self):
        # "➡ ⬅ ⬆ ⬇ ↗ ↘ ↙ ↖"
        row = ""
        for i in range(self.size):
            line1 = ""
            line2 = ""
            line3 = ""
            for j in range(self.size):
                lines = self._cell(self.nodes[i][j]).split("\n")
                line1 += lines[0]
                line2 += lines[1]
                line3 += lines[2]
            row += f"{line1}\n{line2}\n{line3}"
            row += " " if j is not self.size - 1 else ""
            row += "\n" if i is not self.size - 1 else ""
        return row

    def _cell(self, node):
        output = ""
        letter = node.letter
        trans = node.possible_transitions()
        symbols = {
            "up": " ⬆ ",
            "down": " ⬇ ",
            "right": " ➡ ",
            "left": " ⬅ ",
            "upRight": " ↗ ",
            "upLeft": " ↖ ",
            "downRight": " ↘ ",
            "downLeft": " ↙ "
        }
        spacing = "  "

        output += symbols["upLeft"] if "upLeft" in trans else spacing
        output += symbols["up"] if "up" in trans else spacing
        output += symbols["upRight"] if "upRight" in trans else spacing
        output += "\n"

        output += symbols["left"] if "left" in trans else spacing
        output += letter + " "
        output += symbols["right"] if "right" in trans else spacing
        output += "\n"

        output += symbols["downLeft"] if "downLeft" in trans else spacing
        output += symbols["down"] if "down" in trans else spacing
        output += symbols["downRight"] if "downRight" in trans else spacing
        output += "\n"

        return output

    def __init__(self, board, size=4):
        self.size = size
        self.nodes = [[{} for i in range(4)] for j in range(4)]

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
