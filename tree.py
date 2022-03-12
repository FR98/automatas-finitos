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
        return """
\t{data}
{left}\t{right}
            """.format(
                data = self.data,
                left = self.left,
                right = self.right,
            )
        if self.left is not None and self.right is not None:
            return """
\t{data}
{left}:{data}\t{right}:{data}
            """.format(
                data = self.data,
                left = self.left,
                right = self.right,
            )
        elif self.left is None and self.right is None:
            return """
\t{data}
            """.format(
                data = self.data,
            )


