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

        # if st[0] == node.data:
        #     while (st and st[0] == node.data):  # lookahead to see if words are reused
        #         st = st[1:]
        #         if st:
        #             if st[0] not in node.children:
        #                 newNode = WTNode(st[0], None)
        #                 node.children[st[0]] = newNode
        #             node = node.children[st[0]]
        #     if st:
        #         return self.addToBranch(st[1:], node.children[st[0]])
        #     else:
        #         node.isWord = True
        #         return

        if st[0] not in node.children:
            newNode = WTNode(st[0], None)
            node.children[st[0]] = newNode
        return self.addToBranch(st[1:], node.children[st[0]])

    # adds the string st in the tree
    def add(self, st):
        if st:
            # if self.root is None:
            #     nodes = [WTNode(st[-1], None)]
            #     for i in range(len(st) - 2, -1, -1):
            #         nodes.append(WTNode(st[i], nodes[len(st) - i - 2]))
            #     nodes[0].isWord = True
            #     self.nodes[nodes[-1].data] = nodes[-1]
            # else:
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
