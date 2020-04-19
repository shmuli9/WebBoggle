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
        self.root = None

    def __str__(self):
        return str(self.root)

    def addToBranch(self, st, node):
        if not st:  # base case, string is empty
            node.isWord = True
            return

        if st[0] == node.data:
            while (st and st[0] == node.data): # lookahead to see if words are reused
                st = st[1:]
                if st:
                    if st[0] not in node.children:
                        newNode = WTNode(st[0], None)
                        node.children[st[0]] = newNode
                    node = node.children[st[0]]
            if st:
                return self.addToBranch(st[1:], node.children[st[0]])
            else:
                node.isWord=True
                return

        if st[0] not in node.children:
            newNode = WTNode(st[0], None)
            node.children[st[0]] = newNode
        return self.addToBranch(st[1:], node.children[st[0]])

    # adds the string st in the tree and returns None
    def add(self, st):
        if st:
            if self.root is None:
                nodes = [WTNode(st[-1], None)]
                for i in range(len(st) - 2, -1, -1):
                    nodes.append(WTNode(st[i], nodes[len(st) - i - 2]))
                nodes[0].isWord = True
                self.root = nodes[-1]
            else:
                self.addToBranch(st, self.root)
        return None


# wt = WordTree()
# wt.add("cart")
# wt.add("car")
# wt.add("cccc")
# print(wt)

