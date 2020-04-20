class WTNode:
    def __init__(self, string, children: {}):
        self.data = string
        self.isWord = False
        self.children = {}
        if children:
            self.children[children.data] = children

    # prints the node and all its children in a string
    def __str__(self):
        st = "(" + str(self.data) + ", " + str(self.isWord) + ") -> {"
        if self.children is not None:
            st += str(self.children)
        return st + "}"


class WordTree:
    def __init__(self):
        self.children = {}

    def __str__(self):
        return str(self.children)

    def addToBranch(self, st, node):
        if not st:  # base case, string is empty
            node.isWord = True
            return

        chars = st[0]
        remaining = st[1:]
        if chars == "Q":
            chars = "Qu"
            remaining = st[2:]

        if chars not in node.children:
            newNode = WTNode(chars, None)
            node.children[chars] = newNode
        return self.addToBranch(remaining, node.children[chars])

    # adds the string st in the tree
    def add(self, st):
        if len(st) > 2:
            chars = st[0]
            remaining = st[1:]
            if chars == "Q":
                chars = "Qu"
                remaining = st[2:]
            if chars not in self.children:
                newNode = WTNode(chars, None)
                self.children[chars] = newNode
            self.addToBranch(remaining, self.children[chars])

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

        if chars not in self.children:
            return False
        return self._findString(remaining, self.children[chars])


# wt = WordTree()
# wt.add("cart")
# wt.add("art")
# wt.add("car")
# wt.add("cccc")
# wt.add("Queen")
# wt.add("Que")
# wt.add("AQu")
# print(wt)

# print(str(wt.findString("AQu")))
