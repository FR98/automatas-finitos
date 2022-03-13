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

    def add_node(self, temp_root_index, content, left, right, use_head_for):
        if temp_root_index is None:
            if self.current_node_head is None:
                self.current_node_head = Node(content, left, right)
            else:
                if use_head_for == "l":
                    self.current_node_head = Node(content, self.current_node_head, right)
                elif use_head_for == "r":
                    self.current_node_head = Node(content, left, self.current_node_head)
                else:
                    self.current_node_head = Node(content, left, right)
        else:
            if temp_root_index == len(self.temp_roots):
                self.temp_roots.append(Node(content, left, right))
            elif temp_root_index < len(self.temp_roots):
                print("Aver3", temp_root_index)

    def convert_to_binary_tree(self, parent_node, binary_tree_parent=None):
        if binary_tree_parent is None:
            binary_tree_parent = BinaryTreeNode(ord(parent_node.data))

        if parent_node.left is not None and parent_node.left.data is not None:
            binary_tree_parent.left = BinaryTreeNode(ord(parent_node.left.data))
            self.convert_to_binary_tree(parent_node.left, binary_tree_parent.left)

        if parent_node.right is not None and parent_node.right.data is not None:
            binary_tree_parent.right = BinaryTreeNode(ord(parent_node.right.data))
            self.convert_to_binary_tree(parent_node.right, binary_tree_parent.right)

        return binary_tree_parent

    def generate_tree(self):
        regular_ex = self.initial_regular_expression

        self.get_nodes(regular_ex, None)

        print(self.convert_to_binary_tree(self.current_node_head))

    def get_final_of_expression(self, partial_expression):
        i = 0
        while i < len(partial_expression):
            if partial_expression[i] == "(":
                parentheses_counter = 1
                for j in range(i+1, len(partial_expression)):
                    if partial_expression[j] == "(":
                        parentheses_counter += 1
                    elif partial_expression[j] == ")":
                        parentheses_counter -= 1

                    extra = 0
                    if parentheses_counter == 0:
                        if partial_expression[j] == ")":
                            if j + 1 < len(partial_expression):
                                if partial_expression[j+1] == "*" or partial_expression[j+1] == "+" or partial_expression[j+1] == "?":
                                    extra += 2

                            fin = j + extra
                            return fin
            elif regex.match(r"[a-zA-Z*]", partial_expression[i]):
                fin = i
                for j in range(i+1, len(partial_expression)):
                    if not regex.match(r"[a-zA-Z*]", partial_expression[j]):
                        break
                    fin = j
                return fin
            i += 1


    def get_nodes(self, partial_expression, temp_root_index):
        print("Partial expression:", temp_root_index, partial_expression)

        i = 0
        while i < len(partial_expression):
            if partial_expression[i] == "(":
                parentheses_counter = 1
                for j in range(i+1, len(partial_expression)):
                    if partial_expression[j] == "(":
                        parentheses_counter += 1
                    elif partial_expression[j] == ")":
                        parentheses_counter -= 1

                    extra = 0
                    if parentheses_counter == 0:
                        if partial_expression[j] == ")":
                            if j + 1 < len(partial_expression):
                                if partial_expression[j+1] == "*" or partial_expression[j+1] == "+" or partial_expression[j+1] == "?":
                                    extra += 2

                        fin = j + extra
                        init = i + 1
                        self.get_nodes(partial_expression[init:fin], temp_root_index)
                        i = j
                        break
            elif regex.match(r"[a-zA-Z*]", partial_expression[i]):
                fin = i
                for j in range(i+1, len(partial_expression)):
                    if not regex.match(r"[a-zA-Z*]", partial_expression[j]):
                        break
                    fin = j

                for k in range(i, fin + 1):
                    if k + 1 < fin + 1:
                        if k + 2 < fin + 1 and partial_expression[k+2] == "*":
                            self.add_node(
                                temp_root_index,
                                ".",
                                Node(partial_expression[k]),
                                Node("*", Node(partial_expression[k+1]), None),
                                "l"
                            )
                            # fin += 1
                            break
                        else:
                            if partial_expression[k+1] != "*":
                                self.add_node(temp_root_index, ".", Node(partial_expression[k]), Node(partial_expression[k+1]), "l")
                                # fin += 1
                                # break
                            else:
                                fin -= 1
                                break
                    elif len(range(i, fin + 1)) == 1 and regex.match(r"[a-zA-Z]", partial_expression[i]):
                        self.add_node(temp_root_index, partial_expression[k], None, None, "l")
                        break

                i = fin

                if i+1 < len(partial_expression):
                    if partial_expression[i+1] == "*":
                        self.add_node(temp_root_index, "*", Node(partial_expression[i]), None, "l")
                    elif partial_expression[i+1] == "+":
                        self.add_node(temp_root_index, "+", Node(partial_expression[i]), None, "l")
                    elif partial_expression[i+1] == "?":
                        self.add_node(temp_root_index, "?", Node(partial_expression[i]), None, "l")
                    elif partial_expression[i+1] == ")":
                        if i+2 < len(partial_expression):
                            if partial_expression[i+2] == "*":
                                self.add_node(temp_root_index, "*", Node(partial_expression[i]), None, "l")
                            elif partial_expression[i+2] == "+":
                                self.add_node(temp_root_index, "+", Node(partial_expression[i]), None, "l")
                            elif partial_expression[i+2] == "?":
                                self.add_node(temp_root_index, "?", Node(partial_expression[i]), None, "l")

            elif partial_expression[i] == "|":
                fin_sub_re = self.get_final_of_expression(partial_expression[i+1:])
                fin = i + 1 + fin_sub_re + 1
                print("Hola", partial_expression[i+1:fin])
                self.get_nodes(partial_expression[i+1:fin], len(self.temp_roots))
                print("Adios")

                print("g", self.temp_roots)
                if temp_root_index is None:
                    sub_tree_root = self.temp_roots[0]
                    # print("f", self.temp_roots[0])
                else:
                    sub_tree_root = self.temp_roots[temp_root_index + 1]
                    # print("h", self.temp_roots[temp_root_index + 1])

                if sub_tree_root is not None:
                    # binary_sub_tree_root = self.convert_to_binary_tree(sub_tree_root)
                    self.add_node(temp_root_index, "|", Node(partial_expression[i-1]), sub_tree_root, "l")

                if fin < len(partial_expression) and partial_expression[fin] == ")":
                    if fin + 1 < len(partial_expression):
                        if partial_expression[fin + 1] == "*":
                            self.add_node(temp_root_index, "*", Node(partial_expression[fin + 1]), None, "l")
                        elif partial_expression[fin + 1] == "+":
                            self.add_node(temp_root_index, "+", Node(partial_expression[fin + 1]), None, "l")
                        elif partial_expression[fin + 1] == "?":
                            self.add_node(temp_root_index, "?", Node(partial_expression[fin + 1]), None, "l")

                i = i + fin + 1
            else:
                print("-", partial_expression[i])

            # elif i + 2 < len(partial_expression) and partial_expression[i+1] == "|" and regex.match(r"[a-zA-Z]", partial_expression[i+2]):
            #     # a|b
            #     self.add_node("|", partial_expression[i], partial_expression[i+2])
            #     i += 2
            # elif i + 2 < len(partial_expression) and partial_expression[i+1] == "|" and partial_expression[i+2] == "(":
                # self.add_node("|", partial_expression[i], self.get_nodes(self.get_nodes_inside_parenthesis(partial_expression[i+3:])))
                # self.get_nodes_inside_parenthesis(partial_expression[i+3:])
            i += 1



if __name__ == "__main__":
    # re = "(b|b)*abb(a|b)*"
    # w = "babbaaaaa"

    re = "abcd"
    re = "a|b"
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
    re = "a|b*"
    re = "(a|b)*"
    re = "(a|b)*|c"
    re = "(a|b)*c"
    re = "(a|b)*abb"
    re = "ab|cd"
    re = "a|bc"
    re = "a|(bc)"
    # - ERROR
    # re = "a(b)*|c" - No importante
    re = "a|bcd"
    # re = "a|bcde"
    # re = "abc|def"
    # re = "a|(b|cd)"
    # re = "a|(b|c)"
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