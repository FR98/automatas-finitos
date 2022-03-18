# -------------------------------------------------------
# Diseño de Lenguajes de Programación
# Thompson
# Francisco Rosal - 18676
# -------------------------------------------------------

import graphviz
import re as regex

class Transition:
    def __init__(self, val, init, fin):
        self.val = val
        self.init = init
        self.fin = fin

class Thompson:
    def __init__(self, tree):
        self.data = {}
        self.tree = tree
        self.alfabeto = []
        self.transiciones = {}
        self.cantidad_estados = 1
        self.init_estados()

    def init_estados(self):
        cont = 1

        # Se inicializa los estados iniciales y finales de cada transicion
        for i in self.tree.postorder:
            self.data[str(cont)] = Transition(chr(i.value), None, None)
            i.value = cont
            cont += 1

        # Extraigo letras de la expresion
        for hoja in self.tree.leaves:
            if regex.match(r"[a-z]", self.data[str(hoja.value)].val) and self.data[str(hoja.value)].val not in self.alfabeto:
                self.alfabeto.append(self.data[str(hoja.value)].val)

        self.alfabeto.sort()
        self.alfabeto.append("E")

        # Se definen los estados inciales y finales de cada nodo
        for nodo in self.tree.postorder:
            if self.data[str(nodo.value)].val == ".":
                self.data[str(nodo.right.value)].init = self.data[str(nodo.left.value)].fin
                self.data[str(nodo.value)].init = self.data[str(nodo.left.value)].init
                self.data[str(nodo.value)].fin = self.data[str(nodo.right.value)].fin
            else:
                self.data[str(nodo.value)].init = "S" + str(self.cantidad_estados)
                self.data[str(nodo.value)].fin = "S" + str(self.cantidad_estados + 1)
                self.cantidad_estados += 2

    def draw(self):
        # Transicion inicial
        s0 = Transition(None, "S0", "S1")
        canvas = graphviz.Digraph(comment="AFN")
        canvas.attr(rankdir="LR")

        # Se instancia cada estado con sus posibles transiciones
        for i in range(self.cantidad_estados):
            self.transiciones["S" + str(i)] = {}

            for letra in self.alfabeto:
                self.transiciones["S" + str(i)][letra] = []

        for nodo in self.tree.postorder:
            if self.data[str(nodo.value)].val == "|":
                # Inicial OR a los iniciales de los hijos y finales de los hijos al final OR
                if self.data[str(nodo.left.value)].init == s0.fin:
                    s0.fin = self.data[str(nodo.value)].init

                canvas.node(
                    self.data[str(nodo.value)].init,
                    self.data[str(nodo.value)].init
                )

                canvas.node(
                    self.data[str(nodo.left.value)].init,
                    self.data[str(nodo.left.value)].init
                )

                canvas.node(
                    self.data[str(nodo.right.value)].init,
                    self.data[str(nodo.right.value)].init
                )

                canvas.edge(
                    self.data[str(nodo.value)].init,
                    self.data[str(nodo.left.value)].init,
                    label="E"
                )

                self.transiciones[self.data[str(nodo.value)].init]["E"].append(self.data[str(nodo.left.value)].init)

                canvas.edge(
                    self.data[str(nodo.value)].init,
                    self.data[str(nodo.right.value)].init,
                    label="E"
                )

                self.transiciones[self.data[str(nodo.value)].init]["E"].append(self.data[str(nodo.right.value)].init)

                if self.data[str(nodo.value)].fin == "S" + str(self.cantidad_estados-1):
                    canvas.node(
                        self.data[str(nodo.value)].fin,
                        self.data[str(nodo.value)].fin,
                        shape="doublecircle"
                    )
                else:
                    canvas.node(
                        self.data[str(nodo.value)].fin,
                        self.data[str(nodo.value)].fin
                    )

                canvas.node(
                    self.data[str(nodo.left.value)].fin,
                    self.data[str(nodo.left.value)].fin
                )

                canvas.node(
                    self.data[str(nodo.right.value)].fin,
                    self.data[str(nodo.right.value)].fin
                )

                canvas.edge(
                    self.data[str(nodo.left.value)].fin,
                    self.data[str(nodo.value)].fin,
                    label="E"
                )

                self.transiciones[self.data[str(nodo.left.value)].fin]["E"].append(self.data[str(nodo.value)].fin)

                canvas.edge(
                    self.data[str(nodo.right.value)].fin,
                    self.data[str(nodo.value)].fin,
                    label="E"
                )

                self.transiciones[self.data[str(nodo.right.value)].fin]["E"].append(self.data[str(nodo.value)].fin)

            elif self.data[str(nodo.value)].val == "*":
                # Inicial de Kleene al inicial del hijo y el final del hijo al final de Kleene
                if self.data[str(nodo.left.value)].init == s0.fin:
                    s0.fin = self.data[str(nodo.value)].init

                canvas.node(
                    self.data[str(nodo.value)].init,
                    self.data[str(nodo.value)].init
                )

                canvas.node(
                    self.data[str(nodo.left.value)].init,
                    self.data[str(nodo.left.value)].init
                )

                canvas.edge(
                    self.data[str(nodo.value)].init,
                    self.data[str(nodo.left.value)].init,
                    label="E"
                )

                self.transiciones[self.data[str(nodo.value)].init]["E"].append(self.data[str(nodo.left.value)].init)

                if self.data[str(nodo.value)].fin == "S" + str(self.cantidad_estados-1):
                    canvas.node(
                        self.data[str(nodo.value)].fin,
                        self.data[str(nodo.value)].fin,
                        shape="doublecircle"
                    )
                else:
                    canvas.node(
                        self.data[str(nodo.value)].fin,
                        self.data[str(nodo.value)].fin
                    )

                canvas.node(
                    self.data[str(nodo.left.value)].fin,
                    self.data[str(nodo.left.value)].fin
                )

                canvas.edge(
                    self.data[str(nodo.left.value)].fin,
                    self.data[str(nodo.value)].fin,
                    label="E"
                )

                self.transiciones[self.data[str(nodo.left.value)].fin]["E"].append(self.data[str(nodo.value)].fin)

                canvas.edge(
                    self.data[str(nodo.value)].init,
                    self.data[str(nodo.value)].fin,
                    label="E"
                )

                self.transiciones[self.data[str(nodo.value)].init]["E"].append(self.data[str(nodo.value)].fin)

                canvas.edge(
                    self.data[str(nodo.left.value)].fin,
                    self.data[str(nodo.left.value)].init,
                    label="E"
                )

                self.transiciones[self.data[str(nodo.left.value)].fin]["E"].append(self.data[str(nodo.left.value)].init)

            elif self.data[str(nodo.value)].val == ".":
                pass
            else:
                canvas.node(
                    str(self.data[str(nodo.value)].init),
                    self.data[str(nodo.value)].init
                )

                if str(self.data[str(nodo.value)].fin) == "S" + str(self.cantidad_estados-1):
                    canvas.node(
                        str(self.data[str(nodo.value)].fin),
                        self.data[str(nodo.value)].fin,
                        shape="doublecircle"
                    )
                else:
                    canvas.node(
                        self.data[str(nodo.value)].fin,
                        self.data[str(nodo.value)].fin
                    )

                canvas.edge(
                    self.data[str(nodo.value)].init,
                    self.data[str(nodo.value)].fin, label=self.data[str(nodo.value)].val
                )

                self.transiciones[self.data[str(nodo.value)].init][self.data[str(nodo.value)].val].append(self.data[str(nodo.value)].fin)

        canvas.node(s0.init, s0.init)
        canvas.edge(s0.init, s0.fin, label="E")
        self.transiciones[s0.init]["E"].append(s0.fin)
        canvas.view()
