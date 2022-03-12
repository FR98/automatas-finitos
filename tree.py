# -------------------------------------------------------
# Diseño de Lenguajes de Programación
# Tree
# Francisco Rosal - 18676
# -------------------------------------------------------

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

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
