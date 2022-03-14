# -------------------------------------------------------
# Diseño de Lenguajes de Programación
# Automatas Finitos
# Francisco Rosal - 18676
# -------------------------------------------------------

import re as regex
from node import Node
from binarytree import build

class Tree:
    def __init__(self, initial_regular_expression):
        self.current_node_head = None
        self.temp_roots = []
        self.get_nodes(initial_regular_expression, None)

    def get_tree(self):
        return Node.convert_to_binary_tree(self.current_node_head)

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
                if self.temp_roots[temp_root_index] is None:
                    self.temp_roots[temp_root_index] = Node(content, left, right)
                else:
                    if use_head_for == "l":
                        self.temp_roots[temp_root_index] = Node(content, self.temp_roots[temp_root_index], right)
                    elif use_head_for == "r":
                        self.temp_roots[temp_root_index] = Node(content, left, self.temp_roots[temp_root_index])
                    else:
                        self.temp_roots[temp_root_index] = Node(content, left, right)

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
                    if parentheses_counter == 0 and partial_expression[j] == ")":
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
                        if partial_expression[j] == ")" and j + 1 < len(partial_expression):
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
                            self.add_node(temp_root_index, ".", Node(partial_expression[k]), Node("*", Node(partial_expression[k+1]), None), "l")
                            break
                        else:
                            if partial_expression[k+1] != "*":
                                self.add_node(temp_root_index, ".", Node(partial_expression[k]), Node(partial_expression[k+1]), "l")
                            else:
                                fin -= 1
                                break
                    elif len(range(i, fin + 1)) == 1 and regex.match(r"[a-zA-Z]", partial_expression[i]):
                        self.add_node(temp_root_index, partial_expression[k], None, None, "l")
                        break

                i = fin

                if i + 1 < len(partial_expression):
                    if partial_expression[i+1] == "*" or partial_expression[i+1] == "+" or partial_expression[i+1] == "?":
                        self.add_node(temp_root_index, partial_expression[i+1], Node(partial_expression[i]), None, "l")
                    elif partial_expression[i+1] == ")":
                        if i + 2 < len(partial_expression):
                            if partial_expression[i+2] == "*" or partial_expression[i+2] == "+" or partial_expression[i+2] == "?":
                                self.add_node(temp_root_index, partial_expression[i+2], Node(partial_expression[i]), None, "l")

            elif partial_expression[i] == "|" or partial_expression[i] == ".":
                fin_sub_re = self.get_final_of_expression(partial_expression[i+1:])
                fin = i + 1 + fin_sub_re + 1
                self.get_nodes(partial_expression[i+1:fin], len(self.temp_roots))

                if temp_root_index is None:
                    sub_tree_root = self.temp_roots.pop()
                else:
                    sub_tree_root = self.temp_roots.pop(temp_root_index + 1)


                if sub_tree_root is not None:
                    self.add_node(temp_root_index, partial_expression[i], Node(partial_expression[i-1]), sub_tree_root, "l")

                if fin < len(partial_expression) and partial_expression[fin] == ")":
                    if fin + 1 < len(partial_expression):
                        if partial_expression[fin+1] == "*" or partial_expression[fin+1] == "+" or partial_expression[fin+1] == "?":
                            self.add_node(temp_root_index, partial_expression[fin+1], Node(partial_expression[fin+1]), None, "l")

                i = i + fin + 1
            else:
                print("-", partial_expression[i])
            i += 1



if __name__ == "__main__":
    re = "abcd"
    re = "a|b"
    re = "ab|c"
    re = "(ab)|c"
    re = "abc|d"
    re = "(abc)|d"
    re = "a*"
    re = "a*|c"
    re = "(a)*|b"
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
    re = "a|bc"
    re = "a|(bc)"
    re = "ab|cd"
    re = "a|bcd"
    re = "a|bcde"
    re = "abc|def"
    re = "a|(b|c)"
    re = "a|(b|cd)"
    re = "(c|(d|e))*abb"
    re = "(c|(d|(e|f)))*abc"
    re = "(c|(d|(e|f)))*abb|h"
    re = "(c|(d|e))*abb|(a|b)"
    re = "(a|b)*abb|(c|(d|e))"
    re = "(c|(d|e))*abb.(a|b)"
    re = "(c|(d|e))*.(a|b)"
    re = "((c|(d|e))*).(a|b)"
    re = "(c|(d|e))*.(a|b)"
    re = "(a|b)*abb.(c|(d|e))"
    re = "((b|b)*abb.(a|b)*).(a|b)*"

    # - EXAMEN
    re = "(a|b)*"
    re = "((a|(bb))*)"
    re = "(a|b)*.((a|(bb))*)"
    re = "((a|b)*.((a|(bb))*)).E"
    # re = "((a|b)*.((a|(bb))*)).E#"

    # - EXAMPLE
    re = "(b|b)*abb.(a|b)*" # La del ejemplo de las instrucciones

    re = "(a|b)*abb"
    w = "babbaaaaa"

    ast = Tree(re)
    arbol = ast.get_tree()

    print(arbol)
    print([chr(n.value) for n in arbol.postorder])

    # print(arbol.values)
    # print([chr(n) if n is not None else n for n in arbol.values])
    # root = build(arbol.values)
    # print(root)


"""
42 - *
43 - +
46 - .
63 - ?
69 - E
97 - a
98 - b
99 - c
100 - d
101 - e
102 - f
103 - g
104 - h
124 - |
"""