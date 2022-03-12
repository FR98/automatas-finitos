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

    def add_node(self, content, left, right):
        if self.current_node_head is None:
            self.current_node_head = Node(content, Node(left), Node(right))
        else:
            self.current_node_head = Node(content, self.current_node_head, Node(right))
    
    @classmethod
    def print_tree(cls, root_node):
        print(root_node)

    def convert_to_binary_tree(self, parent_node, binary_tree_parent=None):
        if self.root_binary_tree is None:
            self.root_binary_tree = BinaryTreeNode(ord(parent_node.data))
            binary_tree_parent = self.root_binary_tree

        if parent_node.left is not None:
            binary_tree_parent.left = BinaryTreeNode(ord(parent_node.left.data))
            self.convert_to_binary_tree(parent_node.left, binary_tree_parent.left)

        if parent_node.right is not None:
            binary_tree_parent.right = BinaryTreeNode(ord(parent_node.right.data))
            self.convert_to_binary_tree(parent_node.right, binary_tree_parent.right)

    def generate_tree(self):
        regular_expression = self.initial_regular_expression

        self.get_operations_inside_parenthesis(regular_expression)

        # ASTree.print_tree(self.current_node_head)
        self.convert_to_binary_tree(self.current_node_head)
        print(self.root_binary_tree)
    
    def get_operations_inside_parenthesis(self, partial_expression):
        print("Partial expression: " + partial_expression)
        parentheses_counter = 0
        i = 0
        while i < len(partial_expression):
            # print(i)
            # print(partial_expression[i])
            if partial_expression[i] == '(':
                parentheses_counter += 1
                fin = i
                for j in range(i+1, len(partial_expression)):
                    # print(partial_expression[j])
                    if partial_expression[j] == '(':
                        parentheses_counter += 1
                    elif partial_expression[j] == ')':
                        parentheses_counter -= 1
                        if parentheses_counter == 0:
                            fin = j
                            new_partial_expression = partial_expression[i+1:fin]

                            # if j + 1 < len(partial_expression):
                            #     if partial_expression[j+1] == '*' or partial_expression[j+1] == '+' or partial_expression[j+1] == '?':
                            #         print("HOLA", partial_expression[i+1:j+1])
                            #         new_partial_expression = partial_expression[i+1:j+1]
                            #         fin = j+1

                            # print(new_partial_expression)
                            self.get_operations_inside_parenthesis(new_partial_expression)
                            # print(partial_expression[i+1], partial_expression[j])
                            # print(partial_expression[i+1:j])
                            i = fin
                            break
            else:
                if regex.match(r'[a-zA-Z]', partial_expression[i]):
                    print(partial_expression[i])
                    if i + 1 < len(partial_expression) and regex.match(r'[a-zA-Z]', partial_expression[i+1]):
                        self.add_node(".", partial_expression[i], partial_expression[i+1])
                    elif i + 2 < len(partial_expression) and partial_expression[i+1] == '|' and regex.match(r'[a-zA-Z]', partial_expression[i+2]):
                        self.add_node("|", partial_expression[i], partial_expression[i+2])
                    
                        
                # if i == 0:
                #     break
                # print(partial_expression[i])
            i += 1
 


if __name__ == "__main__":
    # re = "(b|b)*abb(a|b)*"
    # w = "babbaaaaa"

    re = "ab"
    re = "ab|c"
    # re = "b|ab"
    # re = "b|(ab)"
    # re = "(a|b)*abb"
    # re = "(c|(d|e))*abb"
    # re = "(c|(d|e))*abb(a|b)"
    # re = "(a|b)*abb(c|(d|e))"
    w = "baabb"

    ast = ASTree(re)
    ast.generate_tree()

"""
46 - .
124 - |
97 - a
98 - b
99 - c
100 - d
101 - e
"""