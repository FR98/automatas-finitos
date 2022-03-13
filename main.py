# -------------------------------------------------------
# Diseño de Lenguajes de Programación
# Automatas Finitos
# Francisco Rosal - 18676
# -------------------------------------------------------

import re as regex
from tree import Node
from functools import partial
from binarytree import Node as BinaryTreeNode


class ASTree:
    def __init__(self, initial_regular_expression):
        self.initial_regular_expression = initial_regular_expression
        self.current_node_head = None
        self.root_binary_tree = None
        self.temp_roots = []

    def add_node(self, content, left, right, use_head_for):
        if self.current_node_head is None:
            self.current_node_head = Node(content, left, right)
        else:
            if use_head_for == "l":
                self.current_node_head = Node(content, self.current_node_head, right)
            elif use_head_for == "r":
                self.current_node_head = Node(content, left, self.current_node_head)
            else:
                self.current_node_head = Node(content, left, right)

    def convert_to_binary_tree(self, parent_node, binary_tree_parent=None):
        if self.root_binary_tree is None:
            self.root_binary_tree = BinaryTreeNode(ord(parent_node.data))
            binary_tree_parent = self.root_binary_tree

        if parent_node.left is not None and parent_node.left.data is not None:
            binary_tree_parent.left = BinaryTreeNode(ord(parent_node.left.data))
            self.convert_to_binary_tree(parent_node.left, binary_tree_parent.left)

        if parent_node.right is not None and parent_node.right.data is not None:
            binary_tree_parent.right = BinaryTreeNode(ord(parent_node.right.data))
            self.convert_to_binary_tree(parent_node.right, binary_tree_parent.right)

    def generate_tree(self):
        regular_ex = self.initial_regular_expression

        self.get_nodes(regular_ex)

        self.convert_to_binary_tree(self.current_node_head)
        print(self.root_binary_tree)

    def get_nodes(self, partial_expression):
        print("Partial expression:", partial_expression)

        i = 0
        while i < len(partial_expression):
            if partial_expression[i] == '(':
                parentheses_counter = 1
                for j in range(i+1, len(partial_expression)):
                    if partial_expression[j] == '(':
                        parentheses_counter += 1
                    elif partial_expression[j] == ')':
                        parentheses_counter -= 1

                    extra = 0
                    if parentheses_counter == 0:
                        if partial_expression[j] == ')':
                            if j + 1 < len(partial_expression):
                                if partial_expression[j+1] == '*' or partial_expression[j+1] == '+' or partial_expression[j+1] == '?':
                                    extra += 2

                        fin = j + extra
                        self.get_nodes(partial_expression[i+1:fin])
                        i = j
                        break
            elif regex.match(r'[a-zA-Z*]', partial_expression[i]):
                fin = i
                for j in range(i+1, len(partial_expression)):
                    if not regex.match(r'[a-zA-Z*]', partial_expression[j]):
                        break
                    fin = j

                for k in range(i, fin + 1):
                    if k + 1 < fin + 1:
                        if k + 2 < fin + 1 and partial_expression[k+2] == '*':
                            self.add_node(
                                ".",
                                Node(partial_expression[k]),
                                Node("*", Node(partial_expression[k+1]), None),
                                "l"
                            )
                            # fin += 1
                            break
                        else:
                            if partial_expression[k+1] != '*':
                                self.add_node(".", Node(partial_expression[k]), Node(partial_expression[k+1]), "l")
                            else:
                                fin -= 1

                i = fin

                if i+1 < len(partial_expression):
                    if partial_expression[i+1] == '*':
                        self.add_node("*", Node(partial_expression[i]), None, "l")
                    elif partial_expression[i+1] == '+':
                        self.add_node("+", Node(partial_expression[i]), None, "l")
                    elif partial_expression[i+1] == '?':
                        self.add_node("?", Node(partial_expression[i]), None, "l")
                    elif partial_expression[i+1] == ')':
                        if i+2 < len(partial_expression):
                            if partial_expression[i+2] == '*':
                                self.add_node("*", Node(partial_expression[i]), None, "l")
                            elif partial_expression[i+2] == '+':
                                self.add_node("+", Node(partial_expression[i]), None, "l")
                            elif partial_expression[i+2] == '?':
                                self.add_node("?", Node(partial_expression[i]), None, "l")
                
                        

            elif partial_expression[i] == '|':
                self.add_node("|", Node(partial_expression[i-1]), Node(partial_expression[i+1]), "l")

            else:
                print("-", partial_expression[i])

            # elif i + 2 < len(partial_expression) and partial_expression[i+1] == '|' and regex.match(r'[a-zA-Z]', partial_expression[i+2]):
            #     # a|b
            #     self.add_node("|", partial_expression[i], partial_expression[i+2])
            #     i += 2
            # elif i + 2 < len(partial_expression) and partial_expression[i+1] == '|' and partial_expression[i+2] == '(':
                # self.add_node("|", partial_expression[i], self.get_nodes(self.get_nodes_inside_parenthesis(partial_expression[i+3:])))
                # self.get_nodes_inside_parenthesis(partial_expression[i+3:])
            i += 1



if __name__ == "__main__":
    # re = "(b|b)*abb(a|b)*"
    # w = "babbaaaaa"

    re = "abcd"
    re = "ab|c"
    re = "(ab)|c"
    re = "abc|d"
    re = "(abc)|d"
    re = "a*"
    re = "a*|c"
    re = "(a)*|c"
    re = "ab*|c"
    re = "(ab)*|c"
    re = "(ab)+|c"
    re = "(ab)?|c"
    re = "(abcd)|e"
    re = "(abcd)*|e"
    re = "(a|b)*|c"
    # - ERROR
    # re = "a(b)*|c"
    # re = "a|bc"
    # re = "a|(bc)"
    # re = "a|bcd"
    # re = "(a|b)*a"
    # re = "(a|b)*abb"
    # re = "(c|(d|e))*abb"
    # re = "(c|(d|e))*abb(a|b)"
    # re = "(a|b)*abb(c|(d|e))"

    # - EXAMPLE
    # re = "(a|b)*((a|(bb))*E)"
    # re = "(a|b)*((a|(bb))*)"
    # re = "(a|b)*"
    # re = "((a|(bb))*)"
    w = "baabb"

    ast = ASTree(re)
    ast.generate_tree()

    # re = "a(b)*|c" == "ab*|c"
    # re = "(ab)*|c"


"""
42 - *
43 - +
46 - .
63 - ?
97 - a
98 - b
99 - c
100 - d
101 - e
124 - |
"""