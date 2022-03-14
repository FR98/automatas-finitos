# -------------------------------------------------------
# Diseño de Lenguajes de Programación
# Tree
# Francisco Rosal - 18676
# -------------------------------------------------------

from binarytree import Node as BinaryTreeNode

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    @staticmethod
    def convert_to_binary_tree(parent_node, binary_tree_parent=None):
        if binary_tree_parent is None:
            binary_tree_parent = BinaryTreeNode(ord(parent_node.data))

        if parent_node.left is not None and parent_node.left.data is not None:
            binary_tree_parent.left = BinaryTreeNode(ord(parent_node.left.data))
            Node.convert_to_binary_tree(parent_node.left, binary_tree_parent.left)

        if parent_node.right is not None and parent_node.right.data is not None:
            binary_tree_parent.right = BinaryTreeNode(ord(parent_node.right.data))
            Node.convert_to_binary_tree(parent_node.right, binary_tree_parent.right)

        return binary_tree_parent

    def __str__(self):
        if self.left is None and self.right is None:
            return """{data}""".format(
                data = self.data,
            )
        else:
            return """{data}:{left},{right}""".format(
                data = self.data,
                left = self.left.data,
                right = self.right.data,
            )
