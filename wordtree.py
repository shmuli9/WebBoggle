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

        if st[0] not in node.children:
            newNode = WTNode(st[0], None)
            node.children[st[0]] = newNode
        return self.addToBranch(st[1:], node.children[st[0]])

    # adds the string st in the tree
    def add(self, st):
        if len(st) > 2:
            if st[0] not in self.children:
                newNode = WTNode(st[0], None)
                self.children[st[0]] = newNode
            self.addToBranch(st[1:], self.children[st[0]])

    def _findString(self, st, node):
        if not st:  # base case, string is empty or node is empty
            if node:  # return multiplicity
                return node.isWord
            return False

        if st[0] in node.children:
            # if len(st) > 1:  # if there is more of string, recur
            return self._findString(st[1:], node.children[st[0]])
        # return node.children[st[0]].isWord
        return False

    def findString(self, st):
        if st[0] not in self.children:
            return False
        return self._findString(st[1:], self.children[st[0]])

#
# wt = WordTree()
# wt.add("cart")
# wt.add("art")
# wt.add("car")
# wt.add("cccc")
# print(wt)
#
# print(str(wt.findString("cccc")))
